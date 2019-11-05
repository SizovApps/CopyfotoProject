from django import forms
from .models import Prod, Service, Work
from django.core.exceptions import ValidationError


class ProdForm(forms.ModelForm):

    class Meta:
        model = Prod
        fields = ['name', 'price', 'slug', 'author', 'description', 'image']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mb-4 prodInput'}),
            'price': forms.TextInput(attrs={'class': 'form-control mb-4 prodInput'}),
            'slug': forms.TextInput(attrs={'class': 'form-control mb-4 prodInput'}),
            'author': forms.TextInput(attrs={'class': 'form-control mb-4 prodInput'}),
            'description': forms.Textarea(attrs={'class': 'form-control mb-4 prodInput'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError("Slug may not be 'Create'")
        if Prod.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Slug must be unique!')
        return new_slug


class ServicesForm(forms.ModelForm):

    class Meta:
        model = Service
        fields = ['name', 'quantity', 'fill10', 'fill50', 'fill100', 'slug', 'description', 'image']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mb-4 prodInput'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control mb-4 prodInput'}),
            'fill10': forms.TextInput(attrs={'class': 'form-control mb-4 prodInput'}),
            'fill50': forms.TextInput(attrs={'class': 'form-control mb-4 prodInput'}),
            'fill100': forms.TextInput(attrs={'class': 'form-control mb-4 prodInput'}),
            'slug': forms.TextInput(attrs={'class': 'form-control mb-4 prodInput'}),
            'description': forms.Textarea(attrs={'class': 'form-control mb-4 prodInput'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError("Slug may not be 'Create'")
        if Service.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Slug must be unique!')
        return new_slug


class PortfolioForm(forms.ModelForm):

    class Meta:
        model = Work
        fields = ['name', 'slug', 'price', 'timeOfWork', 'description', 'image']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mb-4 prodInput'}),
            'slug': forms.TextInput(attrs={'class': 'form-control mb-4 prodInput'}),
            'price': forms.TextInput(attrs={'class': 'form-control mb-4 prodInput'}),
            'timeOfWork': forms.TextInput(attrs={'class': 'form-control mb-4 prodInput'}),
            'description': forms.Textarea(attrs={'class': 'form-control mb-4 prodInput'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError("Slug may not be 'Create'")
        if Service.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Slug must be unique!')
        return new_slug


class SendForm(forms.Form):
    name = forms.CharField(label='Ваше имя', max_length=100)
    url = forms.CharField(label='Ссылка на диск', max_length=100)
    info = forms.CharField(widget=forms.Textarea, label='Информация о заказе')
    file = forms.FileField()

    name.widget.attrs.update({'class': 'form-control'})
    info.widget.attrs.update({'class': 'form-control'})
    url.widget.attrs.update({'class': 'form-control'})

