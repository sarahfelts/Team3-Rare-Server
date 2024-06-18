from django import forms
from rareapi.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['category', 'title','image_url','content']