from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HTMLtoPDFView

router = DefaultRouter()
router.register(r'form', HTMLtoPDFView)

urlpatterns = [
   path('', include(router.urls)),
]