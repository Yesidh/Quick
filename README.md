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
### User register: create a user, don't need to use JWT. You can use your prefered tool for request:
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
    "password": "ayyyyyy"
}
```
- Response
```
POST /register/
HTTP 201 Created
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept
{
    "email": "alonicea@aja.com",
    "username": "alonicea@aja.com",
    "password": "ayyyyyy"
}
```
### User Login: in this endpoint we start to use JWT in each one of it. The only one doesn't neet it is register.
```
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept
```
- request information
```
url: http://127.0.0.1:8000/login/
Media type: application/json
content:
{
    "email": "alonicea@aja.com",
    "password": "ayyyyyy"
}
```
- Response
```
HTTP 200 OK
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU5OTQ1ODk4OCwianRpIjoiYTM4NjdhYTkxNTliNDA2Mzg5MzU3ZDNmYjBjODI2YzQiLCJ1c2VyX2lkIjoxfQ.IWGkmR8yrWJYfQk_6yK78c1kzMlz-wyUya0wv4uh7oo",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTk5MzcyODg4LCJqdGkiOiI0ZDcyNTkyODcxZjY0ZmE3OGFiZmI1MTZiY2M1MjNhOSIsInVzZXJfaWQiOjF9.770vldsKlprHPFVBlfj3crcIg40BGS323D0AwrD_Jp4"
}
```
now for every request we need to use the access token renderer in the login request.
### Create a client:
```
url: http://127.0.0.1:8000/client/
Allow: GET, POST, PUT, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
```
- GET:
```
[
    {
        "id": 1,
        "document": 11111,
        "first_name": "Jorge",
        "last_name": "Ramirez",
        "email": "jorge@ramirez.com"
    },
    {
        "id": 2,
        "document": 222222,
        "first_name": "Miguel",
        "last_name": "Murillo",
        "email": "miguel@murillo.com"
    },
    {
        "id": 3,
        "document": 333333,
        "first_name": "Ramiro",
        "last_name": "Lagos",
        "email": "ramiro@lagos.com"
    },
    {
        "id": 4,
        "document": 44444,
        "first_name": "Betha",
        "last_name": "Bermudez",
        "email": "bertha@bermudez.com"
    },
    {
        "id": 5,
        "document": 55555,
        "first_name": "Angelica",
        "last_name": "Santos",
        "email": "angelica@santos.com"
    }
]
```
- POST:
  - Request information:
  ```
  {
    "document": 66666,
    "first_name": "Sonia",
    "last_name": "Sanchez",
    "email": "sonia@sanchez.com"
  }
  ```
  - Response:
  ```
  HTTP 201 Created
  Allow: GET, POST, PUT, DELETE, HEAD, OPTIONS
  Content-Type: application/json
  Vary: Accept

  {
    "id": 6,
    "document": 66666,
    "first_name": "Sonia",
    "last_name": "Sanchez",
    "email": "sonia@sanchez.com"
  }
  ```
- PUT:
  - Request information:
  ```
  url: http://127.0.0.1:8000/client/6
  {
    "document": 888888,
    "first_name": "Sonia",
    "last_name": "Sanchez",
    "email": "sonia@sanchez.com"
  }
  ```
  - Response
  ```
  {
    "id": 6,
    "document": 888888,
    "first_name": "Sonia",
    "last_name": "Sanchez",
    "email": "sonia@sanchez.com"
  }
  ```
- Delete:
  - Request information:
  ```
  url: http://127.0.0.1:8000/client/6
  {
    "document": 888888,
    "first_name": "Sonia",
    "last_name": "Sanchez",
    "email": "sonia@sanchez.com"
  }
  ```
  - Response
  ```
  HTTP/1.1 204 No Content
  ```
### crud for Bill:
- GET:
```
HTTP 200 OK
Allow: GET, POST, PUT, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 1,
        "client_id": 5,
        "company_name": "Ultrarapidissimo",
        "nit": 10101010,
        "code": 20
    },
    {
        "id": 2,
        "client_id": 4,
        "company_name": "Panhales Jacinto",
        "nit": 111111,
        "code": 21
    },
    {
        "id": 3,
        "client_id": 3,
        "company_name": "Licorera RR",
        "nit": 121212,
        "code": 22
    },
    {
        "id": 4,
        "client_id": 2,
        "company_name": "Restaurante delicioso pollo",
        "nit": 131313,
        "code": 23
    },
    {
        "id": 5,
        "client_id": 1,
        "company_name": "Cafeteria Don Camilo",
        "nit": 14141414,
        "code": 24
    },
    {
        "id": 6,
        "client_id": 3,
        "company_name": "Licorera RR",
        "nit": 131313,
        "code": 26
    }
```
you can use PUT, POST and DELETE over this endpoint whit the url:
```
http://127.0.0.1:8000/bill/
```
### crud for product:
- GET:
```
HTTP 200 OK
Allow: GET, POST, PUT, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 1,
        "name": "bicicleta",
        "description": "todo terreno, rines de lujo, color rojo."
    },
    {
        "id": 2,
        "name": "Portatil",
        "description": "Apple con bateria de larga duracion."
    },
    {
        "id": 3,
        "name": "Lentes de sol",
        "description": "filtro transition ultra alta definicion."
    },
    {
        "id": 4,
        "name": "Zapatillas",
        "description": "Nike runner."
    },
    {
        "id": 5,
        "name": "Silla bebe",
        "description": "adaptable a automovil."
    }
]
```
you can use PUT, POST and DELETE over this endpoint with the url:
```
http://127.0.0.1:8000/product/
```
### crud for billproduct:
- GET:
```
HTTP 200 OK
Allow: GET, POST, PUT, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "bill_id": {
            "id": 1,
            "client_id": 5,
            "company_name": "Ultrarapidissimo",
            "nit": 10101010,
            "code": 20
        },
        "product_id": {
            "id": 1,
            "name": "bicicleta",
            "description": "todo terreno, rines de lujo, color rojo."
        }
    },
    {
        "bill_id": {
            "id": 2,
            "client_id": 4,
            "company_name": "Panhales Jacinto",
            "nit": 111111,
            "code": 21
        },
        "product_id": {
            "id": 5,
            "name": "Silla bebe",
            "description": "adaptable a automovil."
        }
    },
    {
        "bill_id": {
            "id": 2,
            "client_id": 4,
            "company_name": "Panhales Jacinto",
            "nit": 111111,
            "code": 21
        },
        "product_id": {
            "id": 3,
            "name": "Lentes de sol",
            "description": "filtro transition ultra alta definicion."
        }
    },
    {
        "bill_id": {
            "id": 5,
            "client_id": 1,
            "company_name": "Cafeteria Don Camilo",
            "nit": 14141414,
            "code": 24
        },
        "product_id": {
            "id": 2,
            "name": "Portatil",
            "description": "Apple con bateria de larga duracion."
        }
    },
    {
        "bill_id": {
            "id": 4,
            "client_id": 2,
            "company_name": "Restaurante delicioso pollo",
            "nit": 131313,
            "code": 23
        },
        "product_id": {
            "id": 4,
            "name": "Zapatillas",
            "description": "Nike runner."
        }
    }
]
```
you can use PUT, POST and DELETE over this endpoint with the url:
```
http://127.0.0.1:8000/billproduct
```
## Contributing
-- Yesid Gutierrez - Software Engineer                                          
## Versioning
Quick Interview
## Authors
---Yesid Gutierrez  ingyagutierrez@hotmail.com                                    
                                                                               
 