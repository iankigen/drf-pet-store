# Pest Store TDD Django RESTful API Proof of Concept

#### INSTALLATION

```
$ mkdir django-puppy-store
$ cd django-puppy-store
$ python3.6 -m venv env
$ source env/bin/activate
```

#### ROUTES

| Endpoint | Description |
| ---- | --------------- |
| [GET puppies](#) | Get all puppies. |
| [GET puppies/:id](#) | Get a single puppy. |
| [POST puppies](#) | Add a single puppy. |
| [PUT puppies/:id](#) | Update a single puppy. |
| [DELETE puppies/:id](#) | Delete a single puppy. |
| [GET puppies/?search=q](#) | Search a puppy by name,age,breed or color |
