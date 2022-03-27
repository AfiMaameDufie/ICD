## Table of contents
* [General info](#general-info)
* [Setup](#setup)


# General info
A RESTful API to utilize an internationally recognized set of diagnosis codes(icd-10)


<h2>Setup</h2>
To run the application, please follow the guidlines below
<p>
1. Requirements
 <ul>
  <li>Python3</li>
  <li>Django</li>
  <li>Django Rest Framework</li>
  <li> Django Extensions</li>
  <li>Docker and docker compose</li>
</ul></p>
<p>2. Install python3 and Pipenv</p>

<p>3. Please setup as indicated below:</p>

 
  ### Clone this repository into the directory of your choice
  ```
  git clone https://github.com/AfiMaameDufie/ICD
  ```
  
  ### Move into project folder
   ```
   cd ICD
   ```
  
  ### Build the image and run the container(This will also start the server)
  ```
  docker-compose up -d --build
  ```
  
  ### Migrate database models
  ```
  docker-compose exec web python manage.py migrate
  ```
  
  ### Load the data -- specifically the categories.csv and codes.csv data
  ```
  docker-compose exec web python manage.py runscript generate_categories
  ```
  ```
  docker-compose exec web python manage.py runscript generate_codes
  ```
  
  
  ### Access the lists of diagnosis at
  ```
  http://127.0.0.1:8000/api/v1/diagnosis/
  ```
  ### Access a specific diagnosis at 
  ```
  http://127.0.0.1:8000/api/v1/diagnosis/{id}/
  ```
### Test API 
Unit Tests Command
```
docker-compose exec web python manage.py test api.tests
```