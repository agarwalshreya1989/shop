from django.conf.urls import patterns, include, url

from apps.account.views import RegistrationView, VerifyView, WelcomeView,ProfileView,ProductView

urlpatterns = patterns('',
    url(r'^register/$', RegistrationView.as_view(), name="register"),
    url(r'^verify/(?P<token>[^/]+)/$', VerifyView.as_view(), name="verify"),

    url(r'^login/$', 'django.contrib.auth.views.login', {
        'template_name': 'account/login.html',
        'redirect_field_name': 'next'
        }, name="login"),

    url(r'^logout/$', 'django.contrib.auth.views.logout', {
        'next_page': '/',
        }, name="logout"),
    url(r'^product/$', ProductView.as_view(), name="product"),
    url(r'^Profile/$', ProfileView.as_view(), name="profile"),
    url(r'^', WelcomeView.as_view(), name="welcome"),
    

)
