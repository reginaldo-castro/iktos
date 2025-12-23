from rest_framework.routers import DefaultRouter
from .views import OrdemServicoViewSet, OrdemServicoChecklistViewSet, ChecklistItemViewSet

router = DefaultRouter()
router.register(r'ordens-servico', OrdemServicoViewSet, basename='ordem-servico')
router.register(r'ordens-servico-checklist', OrdemServicoChecklistViewSet, basename='ordens-servico-checklist')
router.register(r'checklist', ChecklistItemViewSet, basename='checklist')

urlpatterns = router.urls
