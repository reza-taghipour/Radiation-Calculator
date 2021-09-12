from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.generics import CreateAPIView
from rest_framework.decorators import api_view
from .serializers import *

def home_view(request, *args, **kwargs):
    return render(request,'home.html')


class Pdd(CreateAPIView):
    authentication_classes = []
    permission_classes = [permissions.AllowAny]
    serializer_class = PddSerializer

    def post(self, request, *args, **kwargs):
        d_max = request.data.get("d_max")
        d = request.data.get("d")
        a = (int(d)/int(d_max))*100
        data = {
            'جواب به درصد': a
        }
        return Response (data)


class rec_to_sq(CreateAPIView):
    authentication_classes = []
    permission_classes = [permissions.AllowAny]
    serializer_class = RecToSq

    def post(self, request, *args, **kwargs):
        a_rec = int(request.data.get("a_rec"))
        p_rec = int(request.data.get("p_rec"))
        a = (4*a_rec)/p_rec
        data = {
            'اندازه ضلع مربع معادل': a
        }
        return Response (data)

class Tar(CreateAPIView):
    authentication_classes = []
    permission_classes = [permissions.AllowAny]
    serializer_class = Tar

    def post(self, request, *args, **kwargs):
        d = int(request.data.get("d"))
        fs = int(request.data.get("fs"))
        a = d/fs
        data = {
            'مقدار tar': a
        }
        return Response (data)

class TarToPdd(CreateAPIView):
    authentication_classes = []
    permission_classes = [permissions.AllowAny]
    serializer_class = TarToPdd

    def post(self, request, *args, **kwargs):
        tar = int(request.data.get("tar"))
        bsf = int(request.data.get("bsf"))
        ssd = int(request.data.get("ssd"))
        d_max = int(request.data.get("d_max"))
        d = int(request.data.get("d"))
        a = (tar * ((ssd + d_max)/(ssd + d))**2 * 100) /bsf
        data = {
            'مقدار معادل pdd': a
        }
        return Response (data)

class SsdToSsd(CreateAPIView):
    authentication_classes = []
    permission_classes = [permissions.AllowAny]
    serializer_class = SsdToSsd

    def post(self, request, *args, **kwargs):
        old_pdd = int(request.data.get("old_pdd"))
        bsf_r = int(request.data.get("bsf_r"))
        bsf_rf = int(request.data.get("bsf_rf"))
        f_minord = int(request.data.get("f_minord"))
        a = (old_pdd * bsf_rf * f_minord) / bsf_r
        data = {
            'برای اس اس دی جدید pdd': a
        }
        return Response (data)
        
class MuSsd(CreateAPIView):
    authentication_classes = []
    permission_classes = [permissions.AllowAny]
    serializer_class = MuSsd


    def post(self, request, *args, **kwargs):
        td = int(request.data.get("td"))
        k = int(request.data.get("k"))
        pdd = int(request.data.get("pdd"))
        sc = int(request.data.get("sc"))
        sp = int(request.data.get("sp"))
        ssd_fac = int(request.data.get("ssd_fac"))
        a = (td*100)/( k * pdd * sc *sp*ssd_fac)
        data = {
            'مانیتو یونیت از تکنیک ssd': a
        }
        return Response (data)

class MuSadTechnique(CreateAPIView):
    authentication_classes = []
    permission_classes = [permissions.AllowAny]
    serializer_class = MuSadTechnique


    def post(self, request, *args, **kwargs):
        td = int(request.data.get("td"))
        k = int(request.data.get("k"))
        tmr = int(request.data.get("tmr"))
        sc = int(request.data.get("sc"))
        sp = int(request.data.get("sp"))
        sad_fac = int(request.data.get("sad_fac"))
        oar = int(request.data.get("oar"))
        a = (td*100)/( k * tmr * sc *sp*sad_fac*oar)
        data = {
            'مانیتو یونیت از تکنیک SAD': a
        }
        return Response (data)



# @api_view(['GET', 'POST'])
# def pdd(request):

#     if request.method == 'GET':
#         serializers = PddSerializer
#         return Response(serializers.data)

#     if request.method == 'POST':
#         d_max = request.GET.get('d_max')
#         d = request.GET.get('d')
#         a = (d_max/d)*100
#         return Response(a)


