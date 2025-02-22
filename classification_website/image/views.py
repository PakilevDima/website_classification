from django.shortcuts import render
from .forms import ResumeForm
# Create your views here.

def upload_image(request):
    if request.method == "POST":
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'classification_asnwer.html')
    else:
        form = ResumeForm
        return render(request, 'file_upload.html', {'form': form})