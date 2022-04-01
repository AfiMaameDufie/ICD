from rest_framework.routers import SimpleRouter
from .views import DiagnosisView, CategoryView



router = SimpleRouter()
router.register('diagnosis', DiagnosisView)
router.register('categories', CategoryView)

urlpatterns = router.urls