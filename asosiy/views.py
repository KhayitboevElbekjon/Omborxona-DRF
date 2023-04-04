from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication

# status codda xatolik kodini chiqarib beradi
from .serializer import *
from .models import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status,filters

class OmborViewSet(ModelViewSet):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    queryset=Ombor.objects.all()
    serializer_class=OmborSerializer
    def get_queryset(self):
        queryset=Ombor.objects.filter(user=self.request.user)
        return queryset
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)
class MahsulotViewSet(ModelViewSet):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    queryset=Mahsulot.objects.all()
    serializer_class=MahsulotSerializer
    def get_queryset(self):
        queryset=Mahsulot.objects.filter(ombor_fk__user=self.request.user)
        return queryset
    def perform_create(self,serializer):
        serializer.save(ombor_fk__user=self.request.user)

class ClientViewSet(ModelViewSet):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    queryset=Client.objects.all()
    serializer_class=ClientSerializer
    def get_queryset(self):
        queryset=Client.objects.filter(ombor_fk__user=self.request.user)
        return queryset
    def perform_create(self,serializer):
        serializer.save(ombor_fk__user=self.request.user)

