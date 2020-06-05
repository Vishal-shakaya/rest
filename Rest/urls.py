from django.urls import path
from Rest import views

urlpatterns =[
path('api-list/',views.Api_view.as_view(),name='api_list'),

]