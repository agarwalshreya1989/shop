from django import forms
from apps.shop.models import Product


class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
   
