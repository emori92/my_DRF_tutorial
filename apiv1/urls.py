from django.urls import path, include
from . import views
# Django REST Framework
from rest_framework import routers


# router
router = routers.DefaultRouter()
router.register('book', views.BookViewSet)


urlpatterns = [
    path('books/', include(router.urls)),
]