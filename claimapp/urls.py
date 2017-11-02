from django.conf.urls import url
from . import views


app_name = 'albums'
urlpatterns=[
    #/music/
    url(r'^index/',views.index, name='index'),
    url(r'^data/(?P<selected_page>.+)/', views.staticpage, name='staticpage'),
    url(r'^data/', views.data, name='data'),
    url(r'^daily/', views.daily, name='daily'),
    url(r'^(?P<selected_claim>.+)/', views.detail, name='detail'),
]
