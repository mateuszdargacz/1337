from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # url(r'^$', 'pro_tips.views.home', name='home'),
    url(r'^accounts/', include('pro_tips.apps.accounts.urls')),

    #include django-admin urls
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),

    #Third-party apps urls
    url(r'', include('social_auth.urls')),

)
