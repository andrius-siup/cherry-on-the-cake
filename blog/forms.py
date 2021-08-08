from django import forms
from .models import Post, Category, BlogPostComment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Post Title',
            'category': 'Category',
            'content': 'Add text here',
            'created_by': 'Created by',
        }

        self.fields['title'].widget.attrs['autofocus'] = True  # cursore start here
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False

        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choises = friendly_names
        # for field_name, field in self.fields.items():
        #     field.widget.attrs['class'] = 'border-black rounded-0'


class BlogPostCommentForm(forms.ModelForm):

    class Meta:
        model = BlogPostComment
        fields = '__all__'  # ('name', 'email', 'content',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'post': 'Choose Post',
            'name': 'Name',
            'email': 'Email Address',
            'content': 'Add text here',
        }

        self.fields['name'].widget.attrs['autofocus'] = True  # cursore start here
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
