from django.db import models

# Create your models here.

class Image(models.Model):
    MODEL_CHOICES = [
        ('rn50', 'ResNet50'),
        ('v16', 'Vgg16')
    ]

    image = models.ImageField(blank=False, upload_to='files/')

    model_classification = models.CharField(max_length=60,
                                            choices=MODEL_CHOICES,
                                             name='model',
                                             verbose_name='Модель для классификации картинки'
                                             )


