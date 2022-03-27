from django.test import TestCase
from ..models import DiagnosisCategory, Diagnosis

class DiagnosisCategoryTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # create Diagnosis Category object
        DiagnosisCategory.objects.create(version='icd-10', code="A00", title="Fever")
        
    def test_diagnosis_details(self):
        category = DiagnosisCategory.objects.get(id=1)
        diagnosis_version = f'{category.version}'
        category_code = f'{category.code}'
        category_title = f'{category.title}'
        self.assertEqual(diagnosis_version, 'icd-10')
        self.assertEqual(category_code, 'A00')
        self.assertEqual(category_title, 'Fever')




class DiagnosisTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # create Diagnosis Category object
        category = DiagnosisCategory.objects.create(code="A00", title="Fever")
        
        # create Diagnosis object
        Diagnosis.objects.create(category=category, diagnosis_code="1",
                                abbreviation_description="Comma-ind anal ret",
                                            full_description="Comma-induced anal retention")


    def test_diagnosis_details(self):
        diagnosis = Diagnosis.objects.get(id=1)
        category = f'{diagnosis.category}'
        diagnosis_code = f'{diagnosis.diagnosis_code}'
        abbreviation_description = f'{diagnosis.abbreviation_description}'
        full_description = f'{diagnosis.full_description}'
        self.assertEqual(category, 'A00')
        self.assertEqual(diagnosis_code, '1')
        self.assertEqual(diagnosis.full_code, 'A001')
        abbreviation_description = f'{diagnosis.abbreviation_description}'
        full_description = f'{diagnosis.full_description}'
        self.assertEqual(category, 'A00')
        self.assertEqual(diagnosis_code, '1')
        self.assertEqual(diagnosis.full_code, 'A001')
        self.assertEqual(abbreviation_description, 'Comma-ind anal ret')
        self.assertEqual(full_description,'Comma-induced anal retention')