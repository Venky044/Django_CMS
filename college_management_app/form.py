from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from django.forms import ModelForm

from .models import (Staffs, Students, MessageToStudent, 
                    MessageToStaff, Events, ContactUs)


class CustomUserCreationForm(UserCreationForm):

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'align':'center', 'placeholder':'password'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'password'}),
    )

    class Meta:
        model = User
        fields = ['first_name', 'username', 'password1', 'password2']

        labels = {
            'first_name': 'Name',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'username': forms.TextInput(attrs={'class':'form-control'}),
        }


class StaffForm(ModelForm):
    class Meta:
        model = Staffs
        fields = ['name', 'email', 'gender', 'education', 'address', 'profile_img', 'bio']

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'gender': forms.Select(attrs={'class':'form-control'}),
            'education': forms.TextInput(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
            'bio': forms.Textarea(attrs={'class':'form-control'}),
        }


class StudentForm(ModelForm):
    class Meta:
        model = Students
        fields = ['name', 'roll_no', 'email', 'course', 'gender', 'address', 'profile_img']

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'roll_no': forms.TextInput(attrs={'class':'form-control', 'placeholder':'ex:bsc001(course+00+no)'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'course': forms.Select(attrs={'class':'form-control'}),
            'gender': forms.Select(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
        }


class MessageToStaffForm(ModelForm):
    class Meta:
        model = MessageToStaff
        fields = ['name', 'email', 'subject', 'body']

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'subject': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        }


class MessageToStudentForm(ModelForm):
    class Meta:
        model = MessageToStudent
        fields = ['name', 'email', 'subject', 'body']

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'subject': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        }


class EventsForm(ModelForm):
    class Meta:
        model = Events
        fields = ['title', 'date', 'description']

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'date': forms.TextInput(attrs={'class':'form-control', 'placeholder':'YYYY-MM-DD HH:MM:SS'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
        }


class ContactUsForm(ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'message']

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'message': forms.Textarea(attrs={'class':'form-control'}),
        }