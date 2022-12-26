from django.db import models
from tinymce import models as tinymce_models

# Create your models here.
class Card(models.Model):
    pretitle = tinymce_models.HTMLField(verbose_name = 'Перед Карточкой', blank=True)
    title = models.CharField(verbose_name = 'Оглавление', max_length=50)
    content = tinymce_models.HTMLField(verbose_name = 'Контент', blank=True)
    
    class Meta:
        verbose_name = "Карточка"
        verbose_name_plural = "Карточки"