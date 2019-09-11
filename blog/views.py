from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Publicacion

# Create your views here.

def listar_pub(request):
    posts = Publicacion.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/post_list.html', {'pubs': posts})
def post_detail(request, pk):
    #Publicacion.objects.get(pk=pk) obtiene el post con el id que venga de pk
    post = get_object_or_404(Publicacion, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
