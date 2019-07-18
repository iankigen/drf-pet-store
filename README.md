# Pest Store TDD Django RESTful API Proof of Concept

#### INSTALLATION

```
$ git clone https://github.com/iankigen/drf-pet-store.git && cd drf-pet-store

Create a virtual environment
$ virtualenv -p python3 envname

Activate the virtual env
$ source envname/bin/activate

Install app requirements
$ pip install -r requirement.txt

$ mv .env_sample .env

UPDATE .env

Run Migrations
$ python manage.py migrate

Run Testcase
$ python manage.py test

Run Server
$ python manage.py runserver
```
Go to  [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

#### ROUTES

| Endpoint | Description |
| ---- | --------------- |
| [GET puppies](#) | Get all puppies. |
| [GET puppies/:id](#) | Get a single puppy. |
| [POST puppies](#) | Add a single puppy. |
| [PUT puppies/:id](#) | Update a single puppy. |
| [DELETE puppies/:id](#) | Delete a single puppy. |
| [GET puppies/?search=q](#) | Search a puppy by name,age,breed or color |
