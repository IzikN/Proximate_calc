from django import forms

class MoistureForm(forms.Form):
    sample_id = forms.CharField(required=False)
    initial_weight = forms.FloatField(label="Initial Weight (g)")
    weight_after_drying = forms.FloatField(label="Weight After Drying (g)")

class AshForm(forms.Form):
    sample_id = forms.CharField(required=False)
    crucible_with_ash = forms.FloatField(label="Weight of Crucible + Ash (g)")
    empty_crucible = forms.FloatField(label="Weight of Empty Crucible (g)")
    sample_weight = forms.FloatField(label="Sample Weight (g)")

class FatForm(forms.Form):
    sample_id = forms.CharField(required=False)
    cup_with_fat = forms.FloatField(label="Weight of Cup + Fat (g)")
    empty_cup = forms.FloatField(label="Weight of Empty Cup (g)")
    sample_weight = forms.FloatField(label="Sample Weight (g)")

class FiberForm(forms.Form):
    sample_id = forms.CharField(required=False)
    crucible_with_digested = forms.FloatField(label="Weight of Crucible + Digested Sample (g)")
    crucible_with_ash = forms.FloatField(label="Weight of Crucible + Ash (g)")
    sample_weight = forms.FloatField(label="Sample Weight (g)")

class ProteinForm(forms.Form):
    sample_id = forms.CharField(required=False)
    sample_titre = forms.FloatField(label="Sample Titre (ml)")
    blank_titre = forms.FloatField(label="Blank Titre (ml)")
    normality = forms.FloatField(label="Normality of Acid")
    sample_weight = forms.FloatField(label="Sample Weight (g)")
