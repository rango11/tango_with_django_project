import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_projects.settings')


import django
django.setup()
from rango.models import Category, Page

def populate():
# First, we will create lists of dictionaries containing the pages we want to add into each category.

# Then we will create a dictionary of dictionaries for our categories.
# This might seem a little bit confusing, but it allows us to iterate
# through each data structure, and add the data to our models.

python_pages = [
    {'title': 'Official Python Tutorial',
    'url':'http://docs.python.org/3/tutorial/'},
    {'title':'How to Think like a Computer Scientist',
    'url':'http://www.greenteapress.com/thinkpython/'},
    {'title':'Learn Python in 10 Minutes',
    'url':'http://www.korokithakis.net/tutorials/python/'} ]

django_pages = [
    {'title':'Official Django Tutorial',
    'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/'},
    {'title':'Django Rocks',
    'url':'http://www.djangorocks.com/'},
    {'title':'How to Tango with Django',
    'url':'http://www.tangowithdjango.com/'} ]

other_pages = [
    {'title':'Bottle',
    'url':'http://bottlepy.org/docs/dev/'},
    {'title':'Flask',
    'url':'http://flask.pocoo.org'} ]

cats = {'Python': {'pages': python_pages},
        'Django': {'pages': django_pages},
        'Other Frameworks':{'pages': other_pages} }

#If you want to add more categories or pages,
#add them to the dictionaries above.

#The code below goes through the cats dictionary, then adds each category,
#and then adds all the associated pages for that category.
#FINISH THIS
