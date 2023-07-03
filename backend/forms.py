from django import forms
from .models import Customer, Purchase

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        # fields = '__all__'
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'mobile',
            'password',
        ]
        widgets = {
            'password': forms.PasswordInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['username'].required = True
        self.fields['email'].required = True
        self.fields['mobile'].required = True
        self.fields['password'].required = True


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'