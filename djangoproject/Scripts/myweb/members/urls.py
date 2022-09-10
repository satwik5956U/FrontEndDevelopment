from django.urls import path
from . import views
urlpatterns=[
    path('translate',views.translate,name="translate"),
    path('',views.index,name="home")
]