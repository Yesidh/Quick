<p>
<img width="180" height="100" src="https://res.cloudinary.com/practicaldev/image/fetch/s--O2cjB-id--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://thepracticaldev.s3.amazonaws.com/i/a3exuz06e9h212pandfr.png" align="right" >
</p>





# :colombia: API CRUD with Django rest framework

## Requirement Skills
- Algorithms
- PEP8 good practices
- Software Architectures
- Database design
- SQL knowledge
- Django Rest_Framework and python knowoledge

## The Situation
- Challenge: Develop a REST API that permits make CRUD operations over entities:
  - Client      [id(pk), document, first_name, last_name, email]
  - Bill        [id(pk), clien_id(FK), company_name, nit, code]
  - Product     [id(pk), name, description]
  - BillProduct [id(pk), bill_id(fk), product_id(fk)]
- Aditional:
  - An endpoint to register users with email and password
  - An endpoint to start sesions with email and password using JSON Web Token.
  - Ensure all endpoints entities with JSON Web Token from header petition.
  - An endpoint to generate/download a CSV file with all Client(document, name, bill quantity) instances.
  - An endpoint to upload a CSV file with Client models and create them.
- Recomendations:
  - Use SQL for queries over ORM.
  - less abstraction level in serializers and views files.

## Built With
- Python3
- Django==3.1.1
- djangorestframework==3.11.1
- djangorestframework-simplejwt==4.4.0
- editors(Emacs and Pycharm)
- OS(Linux Mint)
- virtualenv 15.1.0

========================================================================================
## Using CRUD and endpoints step by step
========================================================================================
```
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
IMPORTANT: this deployment is for linux system, for other SO some things change.
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
```
### Software requirements:
- Make sure that you use python 3: [How to install python 3](https://realpython.com/installing-python/#how-to-install-python-on-linux)
- Make sure that you use virtual enviroments: [How Does a Virtual Environment Work?](https://realpython.com/python-virtual-environments-a-primer/#how-does-a-virtual-environment-work)
- Make sure that you are using git: [Getting Started - Installing Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
### Adding a virtual enviroment:
- Creating virtual enviroment:
```
$ virtualenv .env -p python3
```
we will to use a hidden folder for best practices .env.

### Activate the virtual enviroment:
```
$ source .env/bin/activate
```
### Cloning repositoty:
```
$ git clone https://github.com/Yesidh/Quick.git
```
Now, you have a folder in your local machine called, Quick whit this structure:
```
__________________________________________________________________________________________
|--Quick
| |--cubispro
| | |--crud
| | | |--migrations
| | | | |--...
| | | | |--...
| | | | |--...
| | | |--admin.py
| | | |--apps.py
| | | |--models.py
| | | |--serializers.py
| | | |--test.py
| | | |--urls.py
| | | |--views.py
| | |--csvfiles
| | | |--migrations
| | | | |--...
| | | | |--...
| | | | |--...
| | | |--admin.py
| | | |--apps.py
| | | |--models.py
| | | |--test.py
| | | |--urls.py
| | | |--views.py
| | |--cubispro
| | | |--__init__.py
| | | |--asgi.py
| | | |--settings.py
| | | |--urls.py
| | | |--wsgi.py
| | |--users
| | | |--migrations
| | | | |--...
| | | | |--...
| | | | |--...
| | | |--__init__.py
| | | |--admin.py
| | | |--apps.py
| | | |--models.py
| | | |--serializers.py
| | | |--test.py
| | | |--urls.py
| | | |--views.py
| | |--manage.py
| | |--requirements.txt
| |--.gitignore
| |--README.md
```
_______________________________________________________________________________________

change for folder called Quick  using:
```
$ cd Quick
```
cubispro is the folder project name. Now change to it:

```
$ cd cubispro
```
### Install requirements.txt file:
```
pip install -r requirements.txt
```
Now we have all the software to work with the app.
### Create the database file:
make sure your are in the folde Quick/cubispro and run the command it's important for next commands.
```
$ python manager.py makemigrations
```
after it, use the command:
```
$ python manage.py migrate
```
Now we are ready for run the app.
### run de app:
```
$ python manage.py runserver
```
### User register: for test the endpoint you can use your prefered tool whith data:
```
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept
```
- request information
```
url: http://127.0.0.1:8000/register/
Media type: application/json
conten:
{
    "email": "alonicea@aja.com",
    "username": "alonicea@aja.com"
}
```
Response
```
POST /register/
HTTP 201 Created
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "email": "alonicea@aja.com",
    "username": "alonicea@aja.com"
}
```

## Contributing
-- Yesid Gutierrez - Software Engineer                                          
## Versioning
Quick Interview
## Authors
---Yesid Gutierrez  ingyagutierrez@hotmail.com                                    
                                                                               
 