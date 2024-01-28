**colon3** is a proof-of-concept website that aggregates cat shelter listings, akin to petfinder.com and this is the **django** backend for it. It relies on webscraping with BeautifulSoup4 and this repository scrapes the following polish shelter websites:

- Schronisko dla Zwierząt w Łodzi: 
**[schronisko-lodz.pl](https://schronisko-lodz.pl)**

- "Ciapkowo" Schronisko dla Bezdomnych Zwierząt w Gdyni:
**[ciapkowo.pl](https://ciapkowo.pl)**

- Schronisko dla Bezdomnych Zwierząt Na Paluchu:
**[napaluchu.waw.pl](https://napaluchu.waw.pl)**

- Schronisko dla bezdomnych zwierząt w Lublinie: **[schronisko-zwierzaki.lublin.pl](http://schronisko-zwierzaki.lublin.pl)**

It also features a simple API that returns JSON.

# Running

1. With `pip` install the following dependencies: `Django`, `djangorestframework`, `BeautifulSoup4`, `mysqlclient`
2. Create a file in `./colon3/` called `_secret.py` and define the following variables depending on your database, for example:

        #Can be generated with:
        #from django.core.management.utils import get_random_secret_key
        #print(get_random_secret_key())
        secret_key = 'django-...'

        engine = "django.db.backends.mysql"
        name = "colon3_db"
        user = "colon3_admin"
        password = "password"
        host = "127.0.0.1"
        port = "3306"

3. Migrate database and run server

        $ python manage.py migrate
        $ python manage.py runserver


# Custom commands

Intialize the sources (shelters):

    $ python manage.py initsources

Webscrape the information and add to database:

    $ python manage.py scrapeall

Delete all listings, this is used to do a full refresh:

    $ python manage.py deleteall

# Simple API

Getting all cats:

    http://127.0.0.1:8000/cats/

and a specific cat by id: `http://127.0.0.1:8000/cats/?id=017212b1-d127-45f0-a4aa-b9ae35ef8985`

Getting all cats with full source information:

    http://127.0.0.1:8000/cats/full

and specific one by id: `http://127.0.0.1:8000/cats/full?id=017212b1-d127-45f0-a4aa-b9ae35ef8985`

Getting all sources:

    http://127.0.0.1:8000/cats/sources

and specific one by their url: `http://127.0.0.1:8000/cats/sources?url=ciapkowo.pl`
