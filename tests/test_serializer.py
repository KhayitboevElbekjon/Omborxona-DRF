from unittest import TestCase
from asosiy.serializer import *
from rest_framework.test import APIClient
from asosiy.serializer import *

from asosiy.models import Client,Mahsulot


# class MahsulotTestSerializer(TestCase):
#     def test_mahsulot(self):
#         mahsulot={
#             "id":500,
#             "nom":'KiKi',
#             "brend":"nnn",
#             "narx":60000,
#             "kelgan_sana":"2023-12-02",
#             "miqdor":"50",
#             "ulchov":"dona",
#             "ombor_fk":"ombor"
#         }
#         serializer=MahsulotSerializer(data=mahsulot)
#         assert serializer.is_valid()==True
#         # malumot = serializer.validated_data
#         # assert malumot.get('brend') == "Adidas"

# class ClientTestSerializer(TestCase):
#     def test_client(self):
        # client={
        #     "ism":"Ali",
        #     "nom":"Zakir",
        #     "manzil":"Qo'qon shaxar Farobiy ko'chasi",
        #     "tel":"+998995200391",
        #     "qarz":360000000,
        #     "ombor_fk":"ombor"
        # }
        # serializer=ClientSerializer(data=client)
        # assert serializer.is_valid()==True

class TestClientAPI(TestCase):
    def setUP(self)->None:
        self.client=APIClient()
    def test_client_get(self):
        natija=self.client.get('/client/1')
        assert natija.status_code == 200
        assert natija.data['id']==1
        assert natija.data['ism']==Client.objects.get(id=1).ism
        assert natija.data['manzil']==Client.objects.get(id=1).manzil
        assert natija.data['qarz']==Client.objects.get(id=1).qarz
    def test_client_post(self):
        client={
            "ism":"Ali",
            "nom":"AliExpres",
            "manzil":"Dang'ara tumani Kichik turk qishlog'i",
            "tel":"+998505505151",
            "qarz":36000,
            "ombor_fk":10 # xato  yozldi shu yerda qolga tushush kk
        }
        natija=self.client.post('/client/',data=client)
        assert natija.status_code == 400


class TestMahsulotAPI(TestCase):
    def setUP(self)->None:
        self.client=APIClient()
    def test_mahsulot_get(self):
        natija=self.client.get('/client/3')
        assert natija.status_code == 200
        assert natija.data['id']==3
        assert natija.data['nom']==Mahsulot.objects.get(id=3).nom
        assert natija.data['brend']==Mahsulot.objects.get(id=3).brend
        assert natija.data['miqdor']==Mahsulot.objects.get(id=3).miqdor
    def test_mahsulot_post(self):
        mahsulot={
            "nom":"Cola",
            "brend":"Cola",
            "narx":12000,
            "kelgan_sana":"2023-12-02",
            "miqdor": 1200,
            "ulchov": "dona",
            "ombor_fk": 15,
        }
        natija=self.client.post('/client/',data=mahsulot)
        assert natija.status_code == 400
