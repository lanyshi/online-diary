# Project Blog

For this project, I'm going to create a diary web application using Django framework by following one of Django Girls' tutorials.

* Source code can be found at [Django Girls](https://tutorial.djangogirls.org/en/django_start_project/).

* My operating system: macOS

## Getting Started

### Create Project Space

Create a project workspace, called *project-workspace/* which holds my project content.

Load python3 and activate virtual environment.

Go to *project-workspace/* and run the following command line in terminal:

```
django-admin startproject my_project .
```

### Change Settings

Then I change the settings in *my_project/settings.py*

```
ALLOWED_HOSTS = [ 'my own host' ]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

### Migrate

Now I makemigrations and migrate.

```
python manage.py migrate
```

After that I start an app called *diary* and add it to **INSTALLED_APPS**.

## Start Building Content

Up to this point, the skeleton of my project is basically completed, now I can start building elements.

1. Create a diary post model in diary/models.py

	* I'd like to create a field where users can chose multiple options for their Mood on that day. So I googled how to do this and [this](https://www.youtube.com/watch?v=5jWJBpS0tkg) is what I found.
	
2. Open *diary/admin.py* to register the model with *admin.site.register(Post)*.

3. Before running the server, create a superuser to login to the site.

	* At this point, the site looks good. I can add change and delete a post.
	
4. Next I'm going to create views, which means I'll be adding urls to *urls.py* and also creating templates.

To put all my posts on my *diary/templates/diary/post_list.html*, I assigned all the existing posts into a variable called posts in *diary/views.py*.

Then I use \{% for %\} and \{% endfor %\} to get each post and paste it on my html page.

### Managing Repository Structure

Now the tutorial starts introducing CSS and Bootstrap. This is useful later when my project is nearly done, for now I don't have to worry about it too much.

But before moving on, I need to create a static folder to store all the css files in case I forget in the future.

* The *static/* folder would be in the same directory as *templates/*.

```
      django-workspace               django-workspace
      +---diary                      +---diary
      |   +---migrations                 +---static
      |   +---static                         +---css
      |   +---templates                          +---diary.css
      +---my_project
```

Moving on, I'm going to create a *base.html* file in *diary/templates/diary/*.

Divide my html code into these two files. My *post_list* content goes into *post_list.html*, the rest goes into *base.html*.

### More with Views

Create a URL to a post's detail.

First create a view.

* Add a *post_detail* method to *diary/views.py*.
	
* Add the url to *diary/urls.py* (this is a new file).
	
Create a template for the post details.

* Create a file in *diary/templates/diary/* called *post_detail.html*.

### Work with Forms

We need to deploy forms because we need them to add and edit posts.

Apart from needing to import forms from django packages, the rest of implementation is still the same as previous.

* First create method post_new.

* Then add the url to *diary/urls.py*.

* Create a template in *diary/templates/diary/* called *post_new.html*.

* Same with *post_edit*.

The tutorial ends here, but I feel like there can be more stuff on my site. For example, deleting posts, and sign-up/log-in.

## Adding Features

To build sign up and log in features, I found [this](https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html) site very helpful.

But first, I want to allow posts to be deleted.

### Delete Posts

* Create *post_delete* method in *views.py*. Similar code can be found in [video](https://www.youtube.com/watch?v=8_Chnq4x1vA).

* Create an url for *post_delete* in *urls.py*.

* Create a *post_delete.html* template.

	* Note that this page is only for messages, so I have to import *messages* from django packages.
	
	* More about messages framework can be found [here](https://docs.djangoproject.com/en/2.0/ref/contrib/messages/)
	
### Registration System

Go to *forms.py* in *diary/*.

Add the url to *urls.py*:

```
url(r'^signup/$', views.signup, name='signup'),
```

Then I add *sign_up* in the view.

Now I can create a sign up page *signup.html*.

## Login & Sign Out

Tutorial found [here](https://www.youtube.com/watch?v=exgNlhAPyQ8).

### Login

First I add urls to *urls.py*.

```python
from django.contrib.auth.views import login, logout

url(r'^login/$', login, {'template_name':'diary/login.html'}),
```

Then I create a login template.

After logging in, instead of going to *accounts/profile*, I want to go to *post_list.html*.

* In *final_project/settings.py*, add:

```
#accounts
LOGIN_REDIRECT_URL = 'post_list'
```

### Sign Out

Instead of creating a template for logout, I can just redirect users to the login page when they push the logout button.

```python
url(r'^logout/$', logout, {'next_page':'login'}, name='logout'),
```

## Combine New Elements

The last step is to add the signup, login and logout button to my **base.html**.

In **base.html**, I write something like this:

```html
        {% if user.is_authenticated %}
            ...
        {% else %}
            ...
        {% endif %}
```

Then all there left is decorating the website.

## Takeaways

1. I learned lots about MVC Framework and how the three main components - the model, the view, and the controller - relate to each other.

2. I'm more familiar with Django and Python now. I understand the model-view-template architectural pattern and how to use it to build an application.