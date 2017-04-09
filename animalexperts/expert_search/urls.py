from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from .views import *

urlpatterns = [
    url(r'^$', ExpertSearch.as_view(), name='search'),
    url(r'^contribute/$', ContributeHome.as_view(), name='contribute_home'),
    
    # Authentication views for contributors.
    url(r'^contribute/login/$',
        auth_views.LoginView.as_view(template_name='contributors/login.html'), 
        name='contribute_login'),
    url(r'^contribute/logout/$', contribute_logout,
        name='contribute_logout'),
    url(r'^contribute/password_change/$',
            auth_views.PasswordChangeView.as_view(
                template_name='contributors/password_change.html',
                success_url=reverse_lazy('contribute_password_change_done')
            ), 
            name='contribute_password_change'),
    url(r'^contribute/password_change_done/$',
            auth_views.PasswordChangeDoneView.as_view(
                template_name='contributors/password_change_done.html'), 
            name='contribute_password_change_done'),
]
