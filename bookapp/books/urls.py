from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.PublisherList.as_view(), name='index'),
    url(r'^detail/(?P<pk>\d+)/$', views.PublisherDetail.as_view(), name='publisher_detail'),
    url(r'add/$', views.publisher_new, name='publisher_new'),
]
