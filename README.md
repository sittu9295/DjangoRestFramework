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

    Import apiview and response form restframework

    Create a class that will be the container for all http request methods, which inherits apiview

    GET METHOD:

        This method is used to get single data or a collection of data
        Create a function inside the class with name 'get' which takes the request as parameters
        Create a dummy dataset and return the dataset with response
        Create a url for the views in the urls.py file in the app

        Make a get request call for the api with the url in postman application

        NOTE: we can get individual data by passing the unique id of the data as a parameter

    POST METHOD:

        This method use to send the user submited data to backend
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
    
    Create a class to write api for both linked models as a single unit

    Post Method: one bill data can have one or more bill materials data, first write the code to save the bill data and now with the reference id of the bill save the bill materials data.

    Get Method: 
        1) Get All(id = None): create serializer for bill and bill materials and now create a combined serializer, with this combined serializer we can get a bill and it's materials in single api

        2) Get By Id: use the same combined serializer, but now to get only selected bill and it's materials

    Patch Method: bill and bill materials both can be updated with this single function

    Delete Mehtod: Delete bill and it bill materials will be auto deleted because of ondelete cascade














# Authentication

    Create a new app called Authentication and add its name to installed app list in setting.py file
    pip install djangorestframework-simplejwt and add 'rest_framework_simplejwt' to installed app list in setting.py file
    Add:
        from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
        from rest_framework_simplejwt.views import TokenObtainPairView

        in views.py

    Write a class with TokenObtainPairSerializer to generate the token data set

    Create a serializer class with TokenObtainPairView to get the generated token data set

    Create urls.py file and make initial setup on configuration

    Write url for created serializer class

    Add from rest_framework_simplejwt.views import TokenRefreshView  in urls.py file and write urls to refereh api token

    Rest the default authetication reference in settings.py file by adding

        REST_FRAMEWORK = {
    
            'DEFAULT_AUTHENTICATION_CLASSES': (
                
                'rest_framework_simplejwt.authentication.JWTAuthentication',
            )

        }

    Add from datetime import timedelta in setting.py file

    Now add JWT control setting to settings.py file

        
        SIMPLE_JWT = {
            "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
            "REFRESH_TOKEN_LIFETIME": timedelta(days=90),
            "ROTATE_REFRESH_TOKENS": True,
            "BLACKLIST_AFTER_ROTATION": True,
            "UPDATE_LAST_LOGIN": False,

            "ALGORITHM": "HS256",
            "VERIFYING_KEY": "",
            "AUDIENCE": None,
            "ISSUER": None,
            "JSON_ENCODER": None,
            "JWK_URL": None,
            "LEEWAY": 0,

            "AUTH_HEADER_TYPES": ("Bearer",),
            "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
            "USER_ID_FIELD": "id",
            "USER_ID_CLAIM": "user_id",
            "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",

            "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
            "TOKEN_TYPE_CLAIM": "token_type",
            "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",

            "JTI_CLAIM": "jti",

            "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
            "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
            "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),

            "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
            "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
            "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
            "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
            "SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
            "SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",
        }

    Now run the server and fetch the urls in postman to check the api
