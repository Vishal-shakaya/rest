from django.urls import path,include
from rest_framework.routers import DefaultRouter
from Rest import views

router = DefaultRouter()
router.register('list-view',views.View_set, basename='list_view')
router.register('user-view',views.UserViewSet, basename='user_view')

urlpatterns =[
path('api-list/',views.Api_view.as_view(),name='api_list'),
path('',include(router.urls))

]