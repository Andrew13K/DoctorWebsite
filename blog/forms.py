from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'post_photo', 'title_tag', 'author', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'col-12 col-sm-6 '
                                                     'form-floating '
                                                     'form-control',
                                            'placeholder': ''}),
            'post_photo': forms.TextInput(attrs={'class': 'col-12 col-sm-6 '
                                                          'form-floating '
                                                          'form-control',
                                                 'placeholder': ''}),
            'title_tag': forms.TextInput(attrs={'class': 'col-12 col-sm-6 '
                                                         'form-floating '
                                                         'form-control',
                                                'placeholder': ''}),
            'author': forms.Select(attrs={'class': 'col-12 col-sm-6 '
                                                   'form-floating '
                                                   'form-control',
                                          'placeholder': ''}),
            'body': forms.Textarea(attrs={'class': 'col-12 col-sm-6 '
                                                   'form-floating '
                                                   'form-control',
                                          'style': "height: 200px"}),

        }
