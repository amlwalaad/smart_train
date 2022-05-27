from django.urls import path ,include
from . import views
urlpatterns = [
    path('welcomeshunt/',views.welcomeshunt,name='welcomeshunt'),
    path('shuntLogin/',views.shuntLogin,name='shuntLogin'),
]