import datetime
from django import forms
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
User = get_user_model()

from apps.account.models import EmailVerification
from apps.common import generate_random_string, get_current_site



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password', 'gender', 'country']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])

        if commit:
            user.save()

        verification = EmailVerification(
            user=user,
            token=generate_random_string(32),
            created_on=datetime.datetime.now(),
        )
        verification.save()

        user.email_user('Verify', 'http://%s%s' % (get_current_site().domain, reverse('verify', kwargs={'token': verification.token})))
        return user
