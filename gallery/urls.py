# from django.conf.urls import url
# from . import views


# urlpatterns=[
#     # path('',views.index, name='index'),   
#     url(r'^$', views.index, name='index'),
    
# ]
from django.conf.urls import url
from . import views

urlpatterns=[
    url('',views.index,name = 'index'),
  
]