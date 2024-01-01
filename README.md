A Django project for my full stack web app development college course in Python using Django framework and MySQL database. Users can register and log in as well as create/edit their social profile and to see others' profiles.

Install Django:

    - use command "pip list" or "pip3 list" and check if virtualenv is installed. If not install it using these instructions:
    
    - Installing virtualenv on mac:
        - pip (or pip3) install virtualenv
        - sudo su (put in your mac’s password)
        - virtual django_class ("django_class" in the name of the virtual environment - you can name it whatever you want)
        
    - Installing virtualenv on windows:
        - pip (or pip3) install virtualenv
        - python -m virtualenv django_class
        - virtual django_class ("django_class" in the name of the virtual environment - you can name it whatever you want)
        
    - Then activate virtual environment using these commands
        - source django_class/bin/activate (for windows the command to activate is django_class/scripts/activate)
        
    - Install Django using this command:
        - pip install django
        
    - To see the django version use this command:
        - django-admin --version

Install mysqlclient:

    - pip install mysqlclient

(replace database password in settings.py with your own)
*****

One django project can contain more than one application.

First we create a project using this command ("django_social" is the name of the project - you can replace it with your desired name):
    - django-admin startproject django_social

Use this commands then:
    - cd django_social
    - ls
    - python manage.py runserver

Then, when you open http://127.0.0.1:8000/ in the browser, it says “The install worked successfully! Congratulations!”

Then we create an app using this command ("dj_socialapp" is the name of the app - you can replace it with your desired name):
    - python manage.py startapp dj_socialapp

Then add the app to the settings.py file. (INSTALLED_APPS section)

Inside your app folder, create a folder named "templates". (Note that you cannot use any other name). This folder is where you put in your html files.

When building web applications, you probably want to add some static files like images or css files. Create a folder named "static" inside your app folder. (Note that you cannot use any other name)

******

Command to run server:
- python manage.py runserver

Migration commands: (Whenever you create a new model or update an existing one, you want that change to be reflected in the database. To do this, use the following two migration commands (first make sure manage.py is accessible by using ls command):
- python manage.py makemigrations
- python manage.py migrate

MySQL file can look like this:

CREATE DATABASE django_social_db;

USE django_social_db;

SELECT * FROM auth_user

SELECT * FROM dj_socialapp_user_info;

SET SQL_SAFE_Updates=0;

****
When serving static files in a Django project when DEBUG is set to False (in settings.py), use WhiteNoise and the collectstatic command:

Install WhiteNoise:
To serve static files in production, install WhiteNoise using the following command:
pip install whitenoise

Configure Middleware:
In your settings.py file, add WhiteNoise to the MIDDLEWARE list to make Django aware of it:
MIDDLEWARE = [
    # ... other middleware ...
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

Specify Static Root and URL:
Set the STATIC_ROOT and STATIC_URL properties in your settings.py file. STATIC_ROOT specifies the folder where static files will be collected, and STATIC_URL is the URL to access static files:
STATIC_ROOT = BASE_DIR / 'prodfiles'
STATIC_URL = '/static/'

Collect Static Files:
Use the collectstatic management command to automatically collect and place static files in the specified folder:
python manage.py collectstatic

This command collects static files from all your apps and places them in the prodfiles folder.

Serve Static Files in Production:
With WhiteNoise configured and static files collected, your production server can now serve static files. Make sure your web server (e.g., Nginx or Apache) is configured to serve static files from the STATIC_ROOT folder.
