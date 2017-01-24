from django import forms
from blog.myblog.models import BlogPagePost


class BlogPagePostForm(forms.ModelForm):
    class Meta:
        model = BlogPagePost
        fields = ('post_title', 'text')
