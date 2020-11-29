from django import forms
from myorder.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['username', 'dinner', 'style', 'details', 'people', 'address']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'dinner': forms.Select(attrs={'class': 'form-control'}),
            'style': forms.Select(attrs={'class': 'form-control'}),
            'details': forms.Textarea(attrs={'class': 'form-control', 'rows':10}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'username': '성명',
            'dinner': '디너',
            'style': '디너 스타일',
            'details': '요구사항',
            'address': '주소',
        }