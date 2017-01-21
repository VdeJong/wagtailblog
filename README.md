# Wagtail Blog

## About
This is a Blog built with Python/Django and uses Wagtail as CMS.

## Setup
Make sure you have [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) and [wagtail](http://docs.wagtail.io/en/latest/getting_started/tutorial.html) installed.
   1. `$ git pull https://github.com/VdeJong/wagtailblog.git`
   2. Go to the directory where you saved this repository
   3. Setup virtualenv named wagtailblog `$ virtualenv wagtailblog`
   4. Activate virtualenv `$ source wagtailblog/bin/activate`
   5. Go to the blog directory, blog is the name of the app `$ cd blog`
   6. Start the server `$ python manage.py runserver`, usually at: [http://127.0.0.1:8000/](http://127.0.0.1:8000/) 
