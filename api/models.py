from unicodedata import category
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


class Diagnosis(models.Model):
    category = models.ForeignKey(to=DiagnosisCategory, related_name='diagnosis', on_delete=models.CASCADE)
    diagnosis_code = models.CharField(max_length=10, default='', blank=True)
    full_code = models.CharField(max_length=20)
    abbreviation_description = models.CharField(max_length=500)
    full_description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('full_code',)
    
    def __str__(self):
        return self.full_code
    
    # override save method to auto populate self.full_code field
    def save(self,*args,**kwargs):
        self.full_code = self.category.code + self.diagnosis_code
        super(Diagnosis, self).save(*args, **kwargs)
    