from rest_framework import viewsets

from .models import Diagnosis, DiagnosisCategory
from .serializers import DiagnosisSerializer, DiagnosisCategorySerializer

class DiagnosisView(viewsets.ModelViewSet):
    queryset = Diagnosis.objects.all()
    serializer_class = DiagnosisSerializer

class CategoryView(viewsets.ModelViewSet):
    queryset = DiagnosisCategory.objects.all()
    serializer_class = DiagnosisCategorySerializer
