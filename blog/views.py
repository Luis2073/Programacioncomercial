from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect

from .models import Publicaciones
from .forms import FormPub


# Create your views here.
def listar_pub(request):
    pubs = Publicaciones.objects.filter(fecha_publicacion__lte = timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/listar_pub.html', {'pubs': pubs})

def detalle_pub(request, pk):
    p = get_object_or_404(Publicaciones, pk = pk)
    return render(request, 'blog/detalle_pub.html', {'p': p})

def nueva_pub(request):
    if request.method == "POST":
        f = FormPub(request.POST)
        if f.is_valid():
            p = f.save(commit=False)
            p.autor = request.user
            p.fecha_publicacion = timezone.now()
            p.save()
            return redirect('detalle_pub', pk=p.pk)
    else:
        f = FormPub()
    return render(request, 'blog/nueva_pub.html', {'formulario': f})

def editar_pub(request, pk):
    post = get_object_or_404(Publicaciones, pk = pk)
    if request.method == "POST":
        form = FormPub(request.POST, instance = post)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.fecha_publicacion = timezone.now()
            post.save()
            return redirect('detalle_pub', pk=post.pk)
    else:
        form = FormPub(instance=post)
    return render(request, 'blog/nueva_pub.html', {'formulario': form})
