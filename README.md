# Expense Tracker
this django project will be an 'Expense Tracker'  
Project Team Member:  
Alexandra Jelea  
Kaoru Steinböck  
Gerhard Nägele  

# General information
this project should be following the pep8 formatting standard, which should be
carried out by the used editors [PEP 8](https://www.python.org/dev/peps/pep-0008/)

# Installation
the following commands were run to install this project:

## Setup the dev environment
1. to install or activate the virtualenv we are using [Pipenv](https://pipenv.pypa.io)
  
`pipenv shell`

2. install django. In this case the latest version will be installed.
`pipenv install django`

3. create the project.
`django-admin startproject 'expense_tracker' .`

## Start the project

1. to run or start the project
`python manage.py runserver`

2. open the following website
`http://localhost:8000/`


# to run the project
please run the following commands to start the project

1. to run the virtualenv
`pipenv shell`

2. to install all dependencies
`pipenv install`

3. to run or start the project
`python manage.py runserver`

4. open the following website
`http://localhost:8000/`


# Additional Information
We will push our SQLite database into the git repository for easier debugging
between the developers. If something goes wrong we can still go back to older
commited databases. If we experience any problems we will remove the database
from the repository.

We are aware that a binary file or database should should not be commited.
We are making an exception in this case.

# External Packages
[django-crispy-forms](https://github.com/django-crispy-forms/django-crispy-forms)

[Django](https://getbootstrap.com/docs/4.4/getting-started/introduction/)

# Sources
the following sources have been used in general to create this project
  
[Django documentation](https://docs.djangoproject.com/en/3.0/)
  
[Django for Beginners: Build websites with Python and Django (English Edition)](https://www.amazon.de/Django-Beginners-websites-Python-English-ebook/dp/B079ZZLRRL)
