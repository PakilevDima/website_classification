from django.shortcuts import render
from .forms import ResumeForm
# Create your views here.

def upload_image(request):
    if request.method == "POST":
        pass
    else:
        form = ResumeForm
        return render(request, 'file_upload.html', {'form': form})