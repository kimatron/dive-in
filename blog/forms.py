from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    """
    Form for users to submit comments on a blog post.

    Fields:
        body (str): The content of the comment.
    """
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={'id': 'id_body', 'name': 'body'})
        }
