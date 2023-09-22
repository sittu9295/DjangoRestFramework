# Project Setup:

    Create virtual environment : py -3 -m venv .venv
    Activate the environment : .venv/Scripts/activate
    Install django : pip install django
    Install django rest framework : pip install djangorestframework
    Create django project : django-admin startproject projectname .   [dot to mention current folder]

    Add 'rest_framework' in the installed apps list in the setting file
    Run server to check the basic setup is working : python manage.py runserver
    Turn off the server with : Control + C

# App Setup:

    Create app to write api's : python manage.py startapp appname
    Add appname in the installed apps list in the setting file
    Create urls.py file in the app folder

    URLS.PY SETUP:

        Import path from django urls and views of the app
        Declare urlpatterns variable and assign a empty list to it
        Go to urls.py file in the project folder and import include from django urls
        Include the app's urls in the project urls file
        
    Run server again to check the base routing setup.

# Postman:

    Install postman which will act as a client application that used to make a http request to a backed app


# Basic API's in App Views: [Http Request Methods: Get, Post, Patch, Put, Delete]

    Import apiview and response for restframework

    Create a class that will be the container for all http request methods, which inherits apiview

    GET METHOD:

        This method is used to get single data or a collection of data
        Create a function inside the class with name 'get' which takes the request as parameters
        Create a dummy dataset and return the dataset with response
        Create a url for the views in the urls.py file in the app

        Make a get request call for the api with the url in postman application

        NOTE: we can get individual data by passing the unique id of the data as a parameter

    POST METHOD:

        This method use to send the user submited data to backebd services
        Create a function inside the same class with name 'post' which takes request as a parameter
        Make a print to see the received data which located inside the request.data
        Write a dummy Response

        Now use the same url used for get method in postman, but now change the http request method to post
        Select the body option and set data format to raw and transmission type JSON

# Databse Integration:

    MONGO_DB:

        pip install djongo
        pip install pymongo==3.12.3

        And change the Database setting in the setting.py as follows

        DATABASES = {
            'default': {
                'ENGINE': 'djongo',
                'NAME': 'database_name',
            }
        }

        And run : python manage.py makemigrations
        Then: python manage.py migrate

    MYSQL_DB:

        pip install mysqlclient

        And change the Database setting in the setting.py as follows

        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'database_name',
                'USER': 'root',
                'PASSWORD': 'your_password',
                'HOST':'localhost',
                'PORT':'3306',
            }
        }

        And run : python manage.py makemigrations
        Then: python manage.py migrate

# Models Basic Setup:

    Create a model for customer and product, with return string

    And run : python manage.py makemigrations
    Then: python manage.py migrate

    NOTE: also run two command listed above after every change in the models

# Serializer Setup for Models:

    Create a serializers.py file in the app
    Import serializers for rest framework and models for the app

    Create serializer for each models

# API's for Basic Model:

    Import models and serializers for the app files

    create class that inherit apiview to creat a api that have function to handle common http methods of get, post, patch, put, delete
    Also create urls for the class to make it as a fetchable api

# Creating Linked Models:

    Create two models bill and bill materials
    Bill materials have a foriegn relationship with bill and bill have a foriegn relationship with customer


