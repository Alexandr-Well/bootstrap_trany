from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import File


class DropView(TemplateView):
    template_name = 'main.html'


def upload_file(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        File.objects.create(file=file)
        return HttpResponse('')
    return JsonResponse({'post': 'false'})
