from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from authapp.forms import UserRegisterForm, UserProfilerForm
from authapp.models import User
from mainapp.models import Product


class UserAdminRegisterForm(UserRegisterForm):
    image = forms.ImageField(widget=forms.FileInput(),required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'image', 'first_name', 'last_name', 'age', 'password1', 'password2')


    def __init__(self, *args, **kwargs):
        super(UserAdminRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'


class ProductAdminRegisterForm(ModelForm):
   #image = forms.ImageField(widget=forms.FileInput(), required=False)
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'quantity', 'category')

    def __init__(self, *args, **kwargs):
        super(ProductAdminRegisterForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Введите название'
        self.fields['description'].widget.attrs['placeholder'] = 'Описание'
        self.fields['price'].widget.attrs['placeholder'] = 'Цена'
        self.fields['quantity'].widget.attrs['placeholder'] = 'Кол-во'
        self.fields['category'].widget.attrs['placeholder'] = 'Категория'
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        #self.fields['image'].widget.attrs['class'] = 'custom-file-input'


class UserAdminProfileForm(UserProfilerForm):
    email = forms.EmailField(widget=forms.EmailInput())
    username = forms.CharField(widget=forms.TextInput())

    def __init__(self, *args, **kwargs):
        super(UserAdminProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = False
        self.fields['email'].widget.attrs['readonly'] = False
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'