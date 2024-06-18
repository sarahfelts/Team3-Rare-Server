from django import forms
from rareapi.models import Post

class UserForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['first_name', 'last_name','bio','profile_image_url','email']