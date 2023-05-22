from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from .models import Post

from datetime import datetime

# Create your views here.
def homepage(request):
    template = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)