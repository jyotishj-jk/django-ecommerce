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
12. 12. Use the below command to create the pages app,
    python manage.py startapp pages
13. In the file jkre -> settings.py, under 'INSTALLED_APPS=' add the below for django to recognise the 'pages' as an app.
    'pages.apps.PagesConfig', (PagesConfig from pages -> apps.py)
14. Under the pages directory, create urls.py file
