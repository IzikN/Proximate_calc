from django.db import models

class Result(models.Model):
    ANALYSIS_CHOICES = [
        ('Moisture', 'Moisture'),
        ('Ash', 'Ash'),
        ('Fat', 'Fat'),
        ('Fiber', 'Fiber'),
        ('Protein', 'Protein'),
        ('Nitrogen', 'Nitrogen'),
    ]

    sample_id = models.CharField(max_length=100, blank=True, null=True)
    analysis_type = models.CharField(max_length=50, choices=ANALYSIS_CHOICES)
    result = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.analysis_type} - {self.result}%"
