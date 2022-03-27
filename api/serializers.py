from rest_framework import serializers
from .models import Diagnosis, DiagnosisCategory

class DiagnosisCategorySerializer(serializers.ModelSerializer):
    diagnosis = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='diagnosis-detail')

    class Meta:
        model = DiagnosisCategory
        fields = ('url','id','version', 'code', 'title','diagnosis')


class DiagnosisSerializer(serializers.ModelSerializer):
    version = serializers.CharField(source='category.version', read_only=True)
    category = serializers.SlugRelatedField(queryset=DiagnosisCategory.objects.all(), slug_field='code')
    category_title = serializers.CharField(source='category.title', read_only=True)
    
    class Meta:
        model = Diagnosis
        fields = ('url','id','version', 'category', 'category_title',
                  'diagnosis_code', 'full_code','abbreviation_description', 'full_description')
        read_only_fields = ['full_code']


    