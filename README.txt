I. Setting up the project :-

1. Create a directory jkre_project for the jkre_project
2. Create virtual environment in the current directory by entering the following command in vs code,
    python3 -m venv ./venv
    Note: Using a Python virtual environment is a way to isolate your Python development projects from your system installed Python and other Python environment.
3. Use the following commands to activate and deactivate the virtual environments
    venv\Scripts\activate - To activate the virtual environment
    deactivate - To deactivateactivate the virtual environment
4. Create.gitignore file to ignore the selected files from getting commited (Use gitignore.io website to search for Django)
5. Use the command below to perform the initial commit
    git add . && git commit -m 'Initial Commit'
6. Use the following command to install Django (If u want to install in the virtual env, go into virtual env and run the command)
    pip install django
    Note: django-admin help shows the available subcommands
7. To create the Django project use the below command
    django-admin startproject jkre . (Here the . specifies the current directory)
    Note: Use 'python manage.py help' to view the list of commands that can be used with manage.py (Like Django admin commands)
9. If u want to change the interpreter to Virtual environment(venv) from global, Shift+Ctrl+P -> Search Python: Select interpreter -> And select the version showing (venv)
10. To run the Django server, use the following command,
    python manage.py runserver
11. To check if the server is up and running go to browser and open http://127.0.0.1:8000/ or http://localhost:8000/
    Note: Leave one terminal for the running server and open a new terminal

II. Apps, URL's and templates:-

1. Use the below command to create the pages app,
    python manage.py startapp pages
2. In the file jkre -> settings.py, under 'INSTALLED_APPS=' add the below for django to recognise the 'pages' as an app.
    'pages.apps.PagesConfig', (PagesConfig from pages -> apps.py)
3. Under the pages directory, create urls.py file
4. In the urls.py file, import path to define path of the url from django file using the following command,
    from django.urls import path
5. To bring in the views file and to specify the working of the pages when the url is being called, in urls.py import views
    from . import views (. refers all)
6. In the urls file, add url pattern with an empty path (since this is the root path or the home page)
    We are connecting this to the 'index' method in views and set the name of this URL as 'index'.
7. Now add 'index' member in the views.py by defining a function 'index' taking a 'request' as an argument.
    from django.http import HttpResponse and return return HttpResponse('<h1>Hello world</h1>') (Hello world is a sample text)
8. Now add the URL pattern for the main page in the urls.py file in 'jkre' directory.
    Add the path for home page (pages) as empty and include pages.urls (including urls.py) (Note: import include from django.urls)
9. Now to add the templates, go to settings.py -> 'TEMPLATES' and add the following command to tell python on where to look for, for the templates
    'DIRS': [os.path.join(BASE_DIR, 'templates')],
10. Create a folder 'templates' in the root directory 'jkre_project' and create a subfolder in templates called 'pages'.
    In the subfolder pages, create index.html and about.html for index and about pages.
11. Now add url path for 'about' page in pages -> urls.py by the following command,
    path('about', views.about, name='about'),
12. Now add the method for the about page and change for index page in views.py file.
    def about(request):
    return render(request, 'pages/about(or index).html') 
13. To establish a base layout, create base.html under templates directory use 'Jinja template' (Installable as extension in VS code)
    To extend the base template layout to other html pages(index,about)
    a. Add {% block content %}{% endblock %} in the body of base.html
    b. Add {% extends 'base.html' %}{% block content %} "*Content of that page*" {% endblock %}
14. Create a 'static' folder under 'jkre' containng the static images, css, js and webfont files.
15. In settings.py in 'jkre', add the following to add the static directory to the code
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    STATIC_URL = 'static/'
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'jkre/static')]
16. manage.py has an inbuilt 'collectstatic' package to collect these static files. This will create a static directory in the root directory.
    python manage.py collectstatic
17. Add the style sheet and scripts link (href) to the base.html file.
18. To invoke the sheets and scripts in static folder, do the following
    a. Add '{% load static %}' to invoke static files
    b. In place of the href and src calls add like href="{% static 'css/all.css' %}" instead of href="static/css/all.css"
19. Instead of cluttering our base.html file with markup, we can use partials. Create 'partials' folder in templates.
    Add _navbar.html, _topbar.html and _footer.html and add those files in base.html like below
    {% include 'partials/_topbar.html' %}
    (NOTE: Also load static in these partial files if there are any calls for static files, ex:logo.jpg)
20. If u want the active page to be highlighted dynamically, use if statement as given below,
    {% if '/' == request.path %}
        class="nav-item active mr-3"
    {% else %}
        class="nav-item mr-3"
    {% endif %}
21. Now create the 'listings' and 'realtors' app using 'python manage.py startapp listings/realtors'
22. Now create folders and html files for 'listings' under template directory.
23. Create a urls.py file in 'listings' directory and make that file like that of the urls file of 'pages'
    urlpatterns = [
    path('', views.index, name='listings'), #For listings
    path('<int:listing_id>', views.listing, name='about'), #For singular listings with id
    path('search', views.search, name='search'), #For search in listings
]
24. Now include the listings url in the main urls.py file using the below cmd,
    path('listing/', include('listings.urls')),
25. Add the listings and realtors page config in the settings file in INSTALLED_APPS by adding the cmd below,
    'listings.apps.ListingsConfig',
    'realtors.apps.RealtorsConfig',
26. Create the view methods in the listings->views.py for the urls index(listings), listing and search.
27. Add the HTML code for listing,listings and search.html and extend the base.html to these files
28. If you click on the home when you are in listings page, you should be redirected back to the home page.
    For this, in the breadcrumb part of lisitings.html change the index part like below,
    <a href="{% url 'index' %}">
29. To make the 'Featured Listings' in nav bar point to lsiting app, change the pointing link in navbar.html like below,
    <a class="nav-link" href="{% url 'listings' %}">Featured Listings</a>
    And to add the highlighting of the active page, do similar to home and about in navbar.html itself.

III. Modules, migrations and admin
1. Create a database 'jkredb' in PostgreSQL.
2. Psycopg2 is a PostgreSQL database adapter for the Python programming language.
   It is used to connect Python applications to PostgreSQL databases. Install using the following cmd.
    pip install psycopg2 and pip install psycopg2-binary
3. Add the database configuration in settings.py by including the following,
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'jkredb',
        'USER': 'postgres',
        'PASSWORD': 'XXXXXXXX',
        'HOST': 'localhost'
    }}
4. If your database doesn't exist yet, migrate creates all the necessary tables to match your model definitions.
   Otherwise if the database already exists, migrate updates the existing table definitions to match the model definitions. cmd is,
    python manage.py migrate
5. To create the model for Listings, go to models.py in Listings directory and create a class 'Listing' and in that we create all the necessary properties.
6. Similarly, create the models for realtors as well.
7. Migrations are Django’s way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema.
    To do so, run the command 'python manage.py makemigrations'
    NOTE: Before proceeding to migration, install Pillow (pip install Pillow)
8. Now to add the tables, run the command,
    python manage.py migrate
9. 

