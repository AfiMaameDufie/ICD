from django.urls import URLPattern
from rest_framework.routers import SimpleRouter
from .views import DiagnosisView, CategoryView

app_name = 'api'
router = SimpleRouter()
router.register('diagnosis', DiagnosisView)
router.register('categories', CategoryView)

urlpatterns = router.urls