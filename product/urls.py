from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^products/$', views.category_list),
    url(r'^products/(?P<category_slug>.+)/$', views.category_detail, name='category_detail'),
    url(r'^products/(?P<category_slug>.+)/(?P<product_slug>.+)/$', views.product_detail, name='product_detail'),
]
