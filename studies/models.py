

from django.db import models

class Study(models.Model):
    STUDY_PHASE_CHOICES = [
        ('Phase I', 'Phase I'),
        ('Phase II', 'Phase II'),
        ('Phase III', 'Phase III'),
        ('Phase IV', 'Phase IV'),
    ]
    
    study_id = models.AutoField(primary_key=True)
    study_name = models.CharField(max_length=255)
    study_description = models.TextField()
    study_phase = models.CharField(max_length=10, choices=STUDY_PHASE_CHOICES)
    sponsor_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.study_name