from django.db import models

class DiagnosisCategory(models.Model):
    DIAGNOSIS_CODES = (
        ('icd-9', 'ICD-9 2012'),
        ('icd-10', 'ICD-10 2022'),
        ('icd-11', 'ICD-11 2022'),
    )

    version = models.CharField(max_length=20, choices=DIAGNOSIS_CODES, default='icd-10')
    code = models.CharField(unique=True, max_length=10)
    title = models.CharField(max_length=500)


    class Meta:
        ordering = ('title',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
    def __str__(self):
        return self.code

