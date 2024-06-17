from django import forms
from rareapi.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['subject', 'content']