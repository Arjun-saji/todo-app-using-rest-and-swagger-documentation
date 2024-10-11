# Todo App API with Django REST Framework and Swagger

This project is a **Todo application** built using **Django REST Framework (DRF)**. It allows users to perform basic CRUD (Create, Read, Update, Delete) operations on tasks through various methods such as Function-Based Views (FBVs), Class-Based Views (CBVs), Mixins, Generic Views, and ViewSets. The project includes **Swagger** for API documentation and testing.

This project was developed to study how different view types and DRF features work in practice.

## Features

- **CRUD Operations**: Create, read, update, and delete tasks.
- **Multiple View Types**:
  - **Function-Based Views (FBVs)**
  - **Class-Based Views (CBVs)**
  - **Mixins**
  - **Generic Views**
  - **ViewSets**
- **API Documentation**: Integrated with **Swagger** to allow interactive exploration of the API.

  
## Tech Stack

- **Backend**: Django, Django REST Framework
- **API Documentation**: Swagger (using `drf_yasg`)

## Project Setup

### Requirements

- Python 3.x
- Django 4.x
- Django REST Framework
- drf-yasg (for Swagger UI)

### API Endpoints

 Below are the general CRUD endpoints. Specific implementations may differ based on the view type.

- List Tasks: GET /tasks/
- Create Task: POST /tasks/
- Retrieve Task: GET /tasks/{id}/
- Update Task: PUT /tasks/{id}/
- Delete Task: DELETE /tasks/{id}/
