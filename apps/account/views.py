
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, CreateView, UpdateView, ListView

from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404,render_to_response
from django.contrib.auth import get_user_model
from apps.account.models import EmailVerification, User
from apps.account.forms import UserForm
User = get_user_model()

class WelcomeView(TemplateView):
    template_name = 'account/base.html'

class RegistrationView(CreateView):
    template_name = "account/registration.html"
    form_class = UserForm

    def form_valid(self, form):
        # creating user in the save() model of the form , args=(user.pk, )
        user = form.save()
        self.template_name = 'account/registration.html'
        #return super(RegistrationView, self).form_valid(form)
        return render_to_response("account/registration_done.html")
class ProfileView(TemplateView):
    template_name = 'account/profile.html'

class ProductView(TemplateView):
    template_name = 'product/product.html'


class VerifyView(TemplateView):
    template_name = 'account/verification_done.html'

    def get_context_data(self, **kwargs):
        context = super(VerifyView, self).get_context_data(**kwargs)
        token = kwargs.get('token')
        
        try:
            verification = EmailVerification.objects.get(token=token)
            user = verification.user
            user.is_active = True
            user.save()
            verification.delete()
        except EmailVerification.DoesNotExist:
            self.template_name = 'account/verification_fail.html'
        return context




