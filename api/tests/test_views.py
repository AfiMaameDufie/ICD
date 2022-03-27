from urllib import response
from django.utils.http import urlencode
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ..models import DiagnosisCategory, Diagnosis

class TestDiagnosisListCreate(APITestCase):
    def setUp(self):
        self.diagnosis_list_create_url = reverse('diagnosis-list')
        self.diagnosis_detail_url = reverse('diagnosis-detail', args=[1])
        
    def test_get_diagnosis_list(self):
        response = self.client.get(self.diagnosis_list_create_url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual([], response.data['results'])
        
    def test_post_diagnosis(self):
        category = DiagnosisCategory.objects.create(version='icd-10', code="A00", 
                                                  title="Cholera")

        data = {      
            'category':category.code,
            'diagnosis_code':'0',
            'abbreviation_description':'Cholera due to Vibrio cholerae 01, biovar cholerae',
            'full_description': 'Cholera due to Vibrio cholerae 01, biovar cholerae'
            }
        response = self.client.post(self.diagnosis_list_create_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Diagnosis.objects.count(), 1)
        self.assertEqual(Diagnosis.objects.get().full_code, "A000")
        
    

class TestDiagnosisRetrieveUpdateDestroyByID(APITestCase):
    def setUp(self):
        self.diagnosis_list_create_url = reverse('diagnosis-list')
        self.diagnosis_detail_url = 'diagnosis-detail'
        self.category = DiagnosisCategory.objects.create(version='icd-10', code="A00", 
                                                  title="Cholera")
        self.post_diagnosis={
            'category':self.category.code,
            'diagnosis_code':'1',
            'abbreviation_description':'Cholera due to Vibrio',
            'full_description': 'Cholera due to Vibrio cholerae 01, biovar cholerae'
        }
    
    def test_get_diagnosis_by_id(self):
        post_response = self.client.post(self.diagnosis_list_create_url, 
                                         self.post_diagnosis, format='json')
        url = reverse(self.diagnosis_detail_url, None, {post_response.data['id']})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    
    def test_update_existing_diagnosis_object(self):
        post_response = self.client.post(self.diagnosis_list_create_url, 
                                         self.post_diagnosis, format='json')
        url = reverse(self.diagnosis_detail_url, None, {post_response.data['id']})
        data_update = {
            'category':self.category.code,
            'diagnosis_code':'8',
            'abbreviation_description':'Cholera due to Vibrio',
            'full_description': 'Cholera due to Vibrio cholerae'
        }
        update_response = self.client.put(url, data_update, form='json')
        self.assertEqual(update_response.status_code, status.HTTP_200_OK)
        self.assertEqual(update_response.data['diagnosis_code'], '8')
        
    def test_delete_diagnosis_object(self):
        post_response = self.client.post(self.diagnosis_list_create_url, 
                                         self.post_diagnosis, format='json')
        url = reverse(self.diagnosis_detail_url, None, {post_response.data['id']})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class TestDiagnosisCategory(APITestCase):
    
    def setUp(self):
        self.category_list_create_url = reverse("diagnosiscategory-list")
        self.category_detail_url = "diagnosiscategory-detail"
    
    def test_get_category_list(self):
        response = self.client.get(self.category_list_create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'], [])

    def test_post_category_data(self):
        data = {
            "version": "icd-10",
            "code": "A00",
            "title": "Cholera",
        }
        response = self.client.post(self.category_list_create_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['code'], 'A00')
        self.assertEqual(response.data['diagnosis'], [])
        
    def test_post_category_returns_status_code_400_for_invalid_data(self):
        invalid_data = {
            "version":"icd-10",
            "code": "A21",
            "title":""
        }
        response = self.client.post(self.category_list_create_url, invalid_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["title"][0], "This field may not be blank.")
        
    def test_get_category_data_by_id(self):
        data = {
            "version": "icd-10",
            "code": "A81",
            "title": "Malaria",
        }
        post_response = self.client.post(self.category_list_create_url, data, format="json")
        self.assertEqual(post_response.status_code, status.HTTP_201_CREATED)
        response = self.client.get(reverse(self.category_detail_url, args=[post_response.data["id"]]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Malaria")
    
    def test_category_details_returns_404_status_code(self):
        response = self.client.get(reverse(self.category_detail_url, args=[404]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_update_existing_category_data(self):
        data = {
            "version": "icd-10",
            "code": "B00",
            "title": "Cholera",
        }
        post_response = self.client.post(self.category_list_create_url, data, format="json")
        self.assertEqual(post_response.status_code, status.HTTP_201_CREATED)
        
        data_update = {
            "version": "icd-10",
            "code": "B00",
            "title": "Asthma",
        }
        response = self.client.put(reverse(self.category_detail_url, args=[post_response.data["id"]]),
                                  data_update, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_delete_existing_category_data(self):
        data = {
            "version": "icd-10",
            "code": "B00",
            "title": "Cholera",
        }
        post_response = self.client.post(self.category_list_create_url, data, format="json")
        self.assertEqual(post_response.status_code, status.HTTP_201_CREATED)
        response = self.client.delete(reverse(self.category_detail_url, args=[post_response.data["id"]]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
