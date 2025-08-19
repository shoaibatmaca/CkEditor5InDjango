from django.shortcuts import render
from writer.forms import CreatePostForm

def home(request):
    form= CreatePostForm()
    return render(request, "writer/home.html", {'form': form})