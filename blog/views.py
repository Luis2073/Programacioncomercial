from django.shortcuts import render

from .models import Publicaciones
from django.utils import timezone

# Create your views here.
def listar_pub(request):
    pubs = Publicaciones.objects.filter(fecha_publicacion__lte = timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/listar_pub.html', {'pubs': pubs})
