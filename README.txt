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
9. Create super user access for the 'admin' page of the website using the cmd.
    python manage.py createsuperuser
    NOTE: User: jyotish, email: jkre@gmail.com, pwd: 123456.
10. Now go into the URL http://127.0.0.1:8000/admin/ and enter your credentials (mentiioned above) to access the admin page.
11. To add "Listings" and "Realtors" in the admin page, go to admin.py, import Listing/Realtor from '.models' and add the following command
    admin.site.register(Listing/Realtor)
12. Now, we can add the listings and the realtors from the admin page.
13. To create a media directory to store media files, go to jkre-> settings.py and enter the following command (like creating dir for static files)
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    MEDIA_URL = 'media/'
14. For the media files to show up in front end, go to jkre ->urls.py and add the following next to urlpatterns
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    NOTE: Import settings and static in urls.py since it is being used
15. Add the data for realtors and listings in the admin page.
16. To modify the admin page, create a folder 'admin' in the templates directory.
17. Create a file 'base_site.html' and add the following cmd in that file to extend the template of the pre-existing admin page.
    {% extends 'admin/base.html' %}
18. Load static as well since we need to involve static files.
19. To override the specific part of the template use '{% block branding %}' and '{% endblock %}' and add the changes to be done inside that.
20. For the Admin->Listiings(overview page) to show more dettails, to add that we need to do the following,
    a. Go to listings->admin.py and add a class LisitngAdming and mention the data that want to be shown as overview.
    b. Also in the 'admin.site.register' pass the ListingAdmin as an argument.
21. To enable to show detailed info if we click on the title of that listing in this overview page,
    Add 'list_display_links = ('id', 'title')' in the ListingAdmin class.
22. To add a filter box for the realtors, add 'list_filter = ('realtor',)' in the ListingAdmin class.
23. To make the 'is_publishable' editable, add 'list_editable = ('is_published',)' in the ListingAdmin class.
24. To include a search field in the same, add search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
    and to add list per view add 'list_per_page = 25' in the ListingAdmin class.

IV. View methods, display and Search
1. To pull the data from listings model (db), go to listings->views.py and do the following steps,
    a. Import .models from listing
    b. In the index func, fetch the listings from the db using 'listings=Listing.objects.all()'
    c. Create a context dictionary and pass the lisitings into dictionary.
    d. Now in return, pass the dictionary as an argument.
    e. To pass the listings model without any error in the views.py, install 'pip install pylint-django'
    f.
2. In listings.html, add a static if else query above the listings html content
3. If the 'if' statement passes through, create a for loop, '{% for listing in listings %}' and pass the basic html for one listing in it.
4. Now, we need to change the listings.html to display dynamic values from the DB.
    Eg: Instead of <h4>12, Mapplewood</h4>, we need to add <h4>{{ listing.title }}</h4>
5. To introduce comma in price, do the following steps,
    a. In listings->settings.py under INSTALLED_APPS add 'django.contrib.humanize'
    b. In listings.html, load humanize ({% load humanize %})
    c. Now, include in the price as, {{ listing.price|intcomma }}
6. Pagination is the process of dividing a document into discrete pages. This is achived in listings page by below steps in views.py
    a. from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
    b. In index func, add the following,
    paginator = Paginator(listings, 3)
    page_number = request.GET.get("page")
    paged_listings = paginator.get_page(page_number)
    c. In the context, change to 'listings' : paged_listings'
7. In order for the paging to reflect in the listings page, add the following in listings.html,
    a. Add an if else loop to go into pagenation if there are extra pages
    b. Add an if else loop for navigating to previous page
    c. Add a for loop to dynamically show the current page
    d. Add an if else loop for navigating to the next page.
8. To order the listings by list date and to remove unpublished listings, add the following in listings->views.py,
    listings=Listing.objects.order_by('-list_date').filter(is_published=True)
9. Now to make the home and index page as a dynamic content, go to views.py in pages and make the following changes.
10. In the index request function add 'listings = Listing.objects.order_by('list_date').filter(is_published=True)[:3]' to display the latest three displays.
11. Not go to index.html and add an if else loop to show the listings
12. If the if loop passes through, add a for loop to dynamically list the listings.
13. Load humanize to show the comma as intended for the prize.
14. Now change the contents dynamically, Eg: Realtor: {{listing.realtor}}
15. To make the about page dynamic as well, go to pages->views.py and change the about function similar to what we did for listings above.
16. In the same func., to show mvp, add the following,
    mvp_realtor = Realtor.objects.filter.all().filter(is_mvp=True)
    context = {'realtors': realtors,
        'mvp_realtors': mvp_realtor} and pass the context as return argument.
17. Now in the about.html, make the changes accordingly to dynamically display the realtors as we did for listings.
18. Now to show the mvp, in the abov.html do the following chages,
    a. Pass an if else loop to check if there is an mvp.
    b. Add a for loop and check for the mvp (to display multiple mvp) and dynamically change the required fields.
19. To build the single listiing page, open listing.html and extend base.html in it and create a block and put the html body in it.
20. In  listings->views.py, add listing and listing id to the context and pass it and the url.
21. Now change the fields to dynamic values. Add an if loop for the listings photos to be skipped if they are not present.
22. Now, to make the search form in home page active, we are going to make the option values in a seperate python file and import them into index.html.
    In the seperate choices.p file, make the options into dictionary values.
23. Add a for loop in index.html for the choices to read all the keys and values in choices file.
24. Now to handle the submit form, make the search.html and channge the form action as follows,
    <form action="{% url 'search' %}"> which will point to search.html
25. To make the form responsive in search page,
    Import the choices in listings->views.py as well (since search would again show listings from listings.html)
26. In the breadcrumb, point the urls to index(for home) and for listings(for listings)
27. For the search form filtering, first create a query set listing in the search funtion in listiings->views.py and get the listings.
    a.Copy paste the if,else and foor loops for the listings in listings.html to search.html
    b.Starting with searching for keywords (for search) and got to listings->views.py
    c. The request made in search is got and checked if there are keywords using if loop
    d. Use 'description__icontains=keywords' and filter out if any of the keywords match anywhere with the description.
    e. To get the exact match for city, use 'description__iexact=city'
    f. Use filtering (bedrooms__lte=bedrooms) to show bedrooms less than or equal to the mentioned one and do for all items
28. To preserve the form input even after obtaining the search result,
    a. Goto listings->views.py and add 'values': request.GET to the context.
    b. Now in the input in the form for keywords, add an attirbute value like, value="{{value.keywords}}" which will preserve that value.
    c. For scroll down options, use if statement to check if key = values.state and if so, it is 'selected' as the option.

V. Accounts and authentication
1. For provisioning accorunts and authorisation, create a 'accounts' app using
   python manage.py startapp accounts
2. Create a template for the accounts(register/login) page. Add 'accounts.apps.AccountsConfig' in settings.py for this new app.
3. Create a urls.py in accounts folder and define the url patterns handled by the accounts page.
4. Goto accounts->views.py to add the view methods for register, login, dashboard and logout.
5. Go to jkre->urls.py to add accounts url and the file it should point to.
6. Go to partials->navbar.html to point the register and login to correct urls like {% url 'register' % }
7. Now add if else loop in navbar.html to hightlight register/login if the request is in that path (if they are in that page).
8. Now, import the content (html body) for register and login pages and extend base.html
9. Change the form action to "{% url 'register/login' %}" and add method as "POST" to post the data in register/login.html
10. When a post request is used in a form, we need to use a CSRF token (security precaution). To do so, add {% csrf_token %} beneath the form tag.
11. To identify if the form request is 'post' or 'get', add if loop in the register and login methods in views.py.
12. Now to set message (alerts) like when pwd doesn't match, go to settings.py and add message tags (PS: Message config are already added in it)
13. Create _alerts.html in partials and give the template and the if and for loops for the message(alerts) using bootstrap theme.
14. Add messages.error() in views.py for the page you want to show the alert for.
15. Now, inlcude the alerts.html in register & login.html
16. Add post method in accounts->views.py for register to get the form values first name, last name etc.
17. Check if passwords,user name and email match, else return an error message and redirect to register page
18. Import User from django.contrib.auth.models for creating user name objects and to store it in DB
19. Include _alerts.html in the index page so that the error is shown when the page is redirected from login/register to index page.
20.
