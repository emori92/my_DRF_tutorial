from django.urls import path, include
from . import views
# Django REST Framework
from rest_framework import routers


# router
router = routers.DefaultRouter()
router.register('books', views.BookViewSet)

app_name = 'apiv1'
urlpatterns = [
    path('', include(router.urls)),
]