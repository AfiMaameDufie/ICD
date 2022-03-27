import os
import csv

from api.models import DiagnosisCategory, Diagnosis
from django.shortcuts import get_object_or_404
module_dir = os.path.dirname(__file__)
file_path = os.path.join(module_dir, 'codes.csv')

def run():
    try:
        with open(file_path, 'r') as csv_file:
            read_csv = csv.reader(csv_file, delimiter=',')
            for count, data in enumerate(read_csv):
                # Load 200 data
                if count == 50:
                    break
                
                    # retrieve category object via title
                category = get_object_or_404(DiagnosisCategory, code=data[0])
                 # Create Diagnosis object
                Diagnosis.objects.create(category=category, diagnosis_code=data[1], full_code=data[2],
                                            abbreviation_description=data[3], full_description=data[4])
            # Dipslay success message if no exception was thrown     
            print("Data suscessfully loaded to Diagnosis model") 
    except Exception as message:
        print(message)