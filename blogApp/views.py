from django.shortcuts import render

import os

# Create your views here.
def index(request):
    md_file = open(os.path.join(os.path.dirname(__file__), 'posts/md_file.md')).read()
    context = {
        'md_file': md_file
    }
    return render(request, 'blogApp/index.html', context)