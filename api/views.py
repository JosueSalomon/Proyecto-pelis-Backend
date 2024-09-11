import json
from typing import Any
from django.http import HttpRequest, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse as HttpResponse
from django.views import View
from .models import *
# Create your views here.


class GeneroView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args , **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request, id=0):
        if(id>0):
            genero=list(Genero.objects.filter(id=id).values())
            if len(genero)>0:
                generos=genero[0]
                datos={'message': 'exito', 'genero':generos}
            else:
                datos={'message': 'Genero no encontrado'}
            return JsonResponse(datos)
        else:
            genero= list(Genero.objects.values())
            if len(genero)>0:
                datos={'message': 'exito', 'generos':genero}
            else:
                datos={'message': 'No se encontro generos'}
            return JsonResponse(datos)

    def post(self,request):
        jd=json.loads(request.body)
        print(jd)
        Genero.objects.create(tipo=jd['tipo'])
        datos={'message': 'Se registro el nuevo genero'}
        return JsonResponse(datos)

    def put(self,request,id):
        jd=json.loads(request.body)
        genero=list(Genero.objects.filter(id=id).values())
        if len(genero)>0:
            gender=Genero.objects.get(id=id)
            gender.tipo=jd['tipo']
            gender.save()
            datos={'message': 'Se actualizo genero'}
        else:
            datos={'message': 'Genero no encontrado'}
        return JsonResponse(datos)

    def delete(self,request,id):
        genero=list(Genero.objects.filter(id=id).values())
        if len(genero) >0:
            Genero.objects.filter(id=id).delete()
            datos = {'message': "exito"}
        else:
            datos={'message': 'Genero no encontrado'}
        return JsonResponse(datos)
