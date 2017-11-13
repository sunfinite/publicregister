from django.conf.urls import url, include
from publicregister import views

urlpatterns = [
    url(r'^$', views.main),
    url(r'^add$', views.add),
    url(r'^verify$', views.verify),
]
