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

12. Use the below command to create the pages app,
    python manage.py startapp pages
13. In the file jkre -> settings.py, under 'INSTALLED_APPS=' add the below for django to recognise the 'pages' as an app.
    'pages.apps.PagesConfig', (PagesConfig from pages -> apps.py)
14. Under the pages directory, create urls.py file
15. In the urls.py file, import path to define path of the url from django file using the following command,
    from django.urls import path
16. To bring in the views file and to specify the working of the pages when the url is being called, in urls.py import views
    from . import views (. refers all)
17. In the urls file, add url pattern with an empty path (since this is the root path or the home page)
    We are connecting this to the 'index' method in views and set the name of this URL as 'index'.
18. Now add 'index' member in the views.py by defining a function 'index' taking a 'request' as an argument.
    from django.http import HttpResponse and return return HttpResponse('<h1>Hello world</h1>') (Hello world is a sample text)
19. Now add the URL pattern for the main page in the urls.py file in 'jkre' directory.
    Add the path for home page (pages) as empty and include pages.urls (including urls.py) (Note: import include from django.urls)
20. Now to add the templates, go to settings.py -> 'TEMPLATES' and add the following command to tell python on where to look for, for the templates
    'DIRS': [os.path.join(BASE_DIR, 'templates')],
21. Create a folder 'templates' in the root directory 'jkre_project' and create a subfolder in templates called 'pages'.
    In the subfolder pages, create index.html and about.html for index and about pages.
22. Now add url path for 'about' page in pages -> urls.py by the following command,
    path('about', views.about, name='about'),
23. Now add the method for the about page and change for index page in views.py file.
    def about(request):
    return render(request, 'pages/about(or index).html') 
24. To establish a base layout, create base.html under templates directory use 'Jinja template' (Installable as extension in VS code)
    To extend the base template layout to other html pages(index,about)
    a. Add {% block content %}{% endblock %} in the body of base.html
    b. Add {% extends 'base.html' %}{% block content %} "*Content of that page*" {% endblock %}
25. 