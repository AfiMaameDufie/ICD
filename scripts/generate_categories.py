import os
import csv

from diagnosis.models import DiagnosisCategory

module_dir = os.path.dirname(__file__)
file_path = os.path.join(module_dir, 'categories.csv')

def run():
    try:
        with open(file_path, 'r') as csv_file:
            read_csv = csv.reader(csv_file, delimiter=',')
            for index, data in enumerate(read_csv):
                # Load 200 data
                if index == 50:
                    break
                
                DiagnosisCategory.objects.create(code=data[0], title=data[1])  
            # Dipslay success message if no exception was thrown     
            print("Data suscessfully loaded to Diagnosis model")     
    except Exception as message:
        print(message)