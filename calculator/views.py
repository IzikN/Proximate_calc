from django.shortcuts import render, redirect
from .forms import MoistureForm, AshForm, FatForm, FiberForm, ProteinForm
from .models import Result

def home(request):
    return render(request, 'home.html')

def moisture(request):
    if request.method == 'POST':
        form = MoistureForm(request.POST)
        if form.is_valid():
            initial_weight = form.cleaned_data['initial_weight']
            weight_after_drying = form.cleaned_data['weight_after_drying']
            sample_id = form.cleaned_data['sample_id']

            moisture_percent = ((initial_weight - weight_after_drying) / initial_weight) * 100
            Result.objects.create(
                sample_id=sample_id,
                analysis_type='Moisture',
                result=moisture_percent
            )
            return redirect('moisture')
    else:
        form = MoistureForm()

    results = Result.objects.filter(analysis_type='Moisture').order_by('-date_created')
    return render(request, 'moisture.html', {'form': form, 'results': results})

def ash(request):
    if request.method == 'POST':
        form = AshForm(request.POST)
        if form.is_valid():
            crucible_with_ash = form.cleaned_data['crucible_with_ash']
            empty_crucible = form.cleaned_data['empty_crucible']
            sample_weight = form.cleaned_data['sample_weight']
            sample_id = form.cleaned_data['sample_id']

            ash_percent = ((crucible_with_ash - empty_crucible) / sample_weight) * 100
            Result.objects.create(
                sample_id=sample_id,
                analysis_type='Ash',
                result=ash_percent
            )
            return redirect('ash')
    else:
        form = AshForm()

    results = Result.objects.filter(analysis_type='Ash').order_by('-date_created')
    return render(request, 'ash.html', {'form': form, 'results': results})

def fat(request):
    if request.method == 'POST':
        form = FatForm(request.POST)
        if form.is_valid():
            cup_with_fat = form.cleaned_data['cup_with_fat']
            empty_cup = form.cleaned_data['empty_cup']
            sample_weight = form.cleaned_data['sample_weight']
            sample_id = form.cleaned_data['sample_id']

            fat_percent = ((cup_with_fat - empty_cup) / sample_weight) * 100
            Result.objects.create(
                sample_id=sample_id,
                analysis_type='Fat',
                result=fat_percent
            )
            return redirect('fat')
    else:
        form = FatForm()

    results = Result.objects.filter(analysis_type='Fat').order_by('-date_created')
    return render(request, 'fat.html', {'form': form, 'results': results})

def fiber(request):
    if request.method == 'POST':
        form = FiberForm(request.POST)
        if form.is_valid():
            crucible_with_digested = form.cleaned_data['crucible_with_digested']
            crucible_with_ash = form.cleaned_data['crucible_with_ash']
            sample_weight = form.cleaned_data['sample_weight']
            sample_id = form.cleaned_data['sample_id']

            fiber_percent = ((crucible_with_digested - crucible_with_ash) / sample_weight) * 100
            Result.objects.create(
                sample_id=sample_id,
                analysis_type='Fiber',
                result=fiber_percent
            )
            return redirect('fiber')
    else:
        form = FiberForm()

    results = Result.objects.filter(analysis_type='Fiber').order_by('-date_created')
    return render(request, 'fiber.html', {'form': form, 'results': results})

def protein(request):
    if request.method == 'POST':
        form = ProteinForm(request.POST)
        if form.is_valid():
            sample_titre = form.cleaned_data['sample_titre']
            blank_titre = form.cleaned_data['blank_titre']
            normality = form.cleaned_data['normality']
            sample_weight = form.cleaned_data['sample_weight']
            sample_id = form.cleaned_data['sample_id']

            nitrogen_percent = ((sample_titre - blank_titre) * 1.4007 * normality) / sample_weight
            protein_percent = nitrogen_percent * 6.25

            # Save Nitrogen separately
            Result.objects.create(
                sample_id=sample_id,
                analysis_type='Nitrogen',
                result=nitrogen_percent
            )
            # Save Protein
            Result.objects.create(
                sample_id=sample_id,
                analysis_type='Protein',
                result=protein_percent
            )
            return redirect('protein')
    else:
        form = ProteinForm()

    results = Result.objects.filter(analysis_type__in=['Protein', 'Nitrogen']).order_by('-date_created')
    return render(request, 'protein.html', {'form': form, 'results': results})
