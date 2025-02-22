from django.shortcuts import render
from django.conf import settings
import os
from .forms import ResumeForm
from .models_classification.resnet50 import ResNet50
from .models_classification.vgg_16 import Vgg16
# Create your views here.

class ModelAnswer:
    def __init__(self, path_image: str, model_name: str):
        self.path_image = path_image
        self.model_name = model_name
        self.class_percent = []
        self.media = settings.MEDIA_ROOT
        self.first = None
        self.first_percent = None
        self.second = None
        self.second_percent = None
        self.path = None

    def get_class_name_percent(self):
        model = None
        if self.model_name == 'v16':
            self.model_name = "Vgg16"
            model = Vgg16()
        else:
            model = ResNet50()
            self.model_name = "ResNet50"
        self.path = str(os.path.join(self.media, 'files', self.path_image))
        data = model.image_classification(path=self.path)
        self.first = list(data.keys())[0]
        self.first_percent = str(float(list(data.values())[0]) * 100)
        self.second = list(data.keys())[1]
        self.second_percent = str(float(list(data.values())[1]) * 100)

def upload_image(request):
    if request.method == "POST":
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            link = str(form.cleaned_data['image'])
            model = ModelAnswer(str(form.cleaned_data['image']), form.cleaned_data['model'])
            model.get_class_name_percent()
            return render(request, 'classification_asnwer.html', {'answer_classification': model})
    else:
        form = ResumeForm
        return render(request, 'file_upload.html', {'form': form})