from django import forms
from blog.models import Post, Comment


class PostFrom(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('author', 'text', 'title')

        """
        in order to add some custom css style to the form, we need to define widget dictionary
        inside it, for each field, we define a class or a list of classes that we want to inherit their
        style 
        """
        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'})
        }


class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('author', 'text')

        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'})
        }
