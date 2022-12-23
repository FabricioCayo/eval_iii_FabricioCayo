from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from mundial_api.models import Equipo, Jugador
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def puntoProtegidoEjemplo(request):
    return Response ({'status':'OK'}, status=status.HTTP_200_OK)


def mostrarEquipos(request):
    equipo = Equipo.objects.all()
    data = {'equipo': equipo}
    return render(request, 'mostrar_equipos.html', data)

def mostrarEquipo(request, id):
    equipo = Equipo.objects.filter(id=id).first()
    data = {'equipo': equipo}
    return render(request, 'mostrar_equipo.html', data)