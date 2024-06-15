from django import forms
from django.forms import fields

from .models import Comment, Article


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment',]
        # widgets = {
        #     'writer':forms.HiddenInput(),
        #     'article':forms.HiddenInput(),
        # }


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title','body')


