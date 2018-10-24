from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Post

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'password1', 'password2', )

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('date', 'weather', 'mood', 'title', 'text',)
