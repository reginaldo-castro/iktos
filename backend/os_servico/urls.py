from rest_framework.routers import DefaultRouter
from .views import OrdemServicoViewSet, OrdemServicoChecklistViewSet, ChecklistItemViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path, include

router = DefaultRouter()
router.register(r'ordens-servico', OrdemServicoViewSet, basename='ordem-servico')
router.register(r'ordens-servico-checklist', OrdemServicoChecklistViewSet, basename='ordens-servico-checklist')
router.register(r'checklist', ChecklistItemViewSet, basename='checklist')

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls))
]