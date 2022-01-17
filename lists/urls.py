from django.conf.urls import url
from lists import views

urlpatterns = [
    url(r'^new$', views.new_list, name='new_list'),
    url(r'^(\d+)/$', views.view_list, name='view_list'), # (.+) is a capture group. The captured text will be passed to the view as an argument.
    url(r'^(\d+)/add_item$', views.add_item, name='add_item'),
]
