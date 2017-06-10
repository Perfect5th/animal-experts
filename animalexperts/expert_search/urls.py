from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from rest_framework.urlpatterns import format_suffix_patterns

from .api import views as api_views
from .views import *

urlpatterns = [
    url(r'^$', ExpertSearch.as_view(), name='search'),
    url(r'^contribute/$', ContributeHome.as_view(), name='contribute_home'),
    url(r'^contribute/add_expert/$', ContributeAddExpert.as_view(), name='contribute_add_expert'),

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

api_urlpatterns = [
    # REST API views.
    url(r'^api/$', api_views.api_root, name='api-root'),
    url(r'^api/experts/$', api_views.ExpertList.as_view(), name='expert-list'),
    url(r'^api/experts/(?P<pk>[0-9]+)/$', api_views.ExpertDetail.as_view(),
        name='expert-detail'),
    url(r'^api/fields/$', api_views.FieldCategoryList.as_view(),
        name='fieldcategory-list'),
    url(r'^api/fields/(?P<code>[A-Za-z0-9_-]+)/$',
        api_views.FieldCategoryDetail.as_view(), name='fieldcategory-detail'),
]

api_urlpatterns = format_suffix_patterns(api_urlpatterns)
urlpatterns = urlpatterns + api_urlpatterns
urlpatterns += [
    # REST API auth urls.
    url(r'^api-auth/', include('rest_framework.urls'))
]
