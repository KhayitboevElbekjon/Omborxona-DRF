from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
   openapi.Info(
      title="Ombor drf API",
      default_version='v1',
      description="Dars davomida amaliyot uchun qilingan Ombor drf API",
      contact=openapi.Contact("Xayitboeyev Elbekjon <backenddevolpment@gmail.com>"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


from django.contrib import admin
from django.urls import path,include

from rest_framework.routers import DefaultRouter
from asosiy.views import *
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

router=DefaultRouter()
router.register('ombor',OmborViewSet)
router.register('mahsulotlar',MahsulotViewSet)
router.register('client',ClientViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('get_token/', TokenObtainPairView.as_view()),
    path('token_yangilash/', TokenRefreshView.as_view()),
    path('docs/',schema_view.with_ui('swagger',cache_timeout=0))
]
