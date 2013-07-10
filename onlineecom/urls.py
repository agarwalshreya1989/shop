

from django.conf.urls import patterns, include, url

from apps.account.views import WelcomeView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'smb.views.home', name='home'),
     url(r'^$', WelcomeView.as_view(), name="base"),
    # url(r'^smb/', include('smb.foo.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^account/', include('apps.account.urls')),
    #url(r'^customer/',include('apps.customer.urls')),
    #url(r'^shipping/',include('apps.shipping.urls')),
    #url(r'^payment/',include('apps.payment.urls')),
    #url(r'^product/',include('apps.product.urls')),
   
   # url(r'^grappelli/', include('grappelli.urls')),
)
