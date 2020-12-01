from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.core.files.base import ContentFile
from django.urls import reverse

from io import BytesIO
from PIL import Image
from urllib import request


class UserFile(models.Model):
    name = models.CharField(
        verbose_name='Название изображения', blank=True, max_length=150)
    url_variable = models.URLField(blank=True, verbose_name='Ссылка')
    image = models.ImageField(
        upload_to='some_directory/', height_field=None, width_field=None, max_length=None, verbose_name='Файл', blank=True)

    # результат обрезки буду сохранять в одно из полей модели
    resized_image = models.ImageField(
        verbose_name='Последнее изменение', blank=True, upload_to='resized_imgs', null=True)

    def get_absolute_url(self):
        return reverse("image_detail", kwargs={"pk": self.pk})

    # В документации Pillow фильтр LANCZOS указан как вариант и для thumbnail, и resize методов.
    # Т.к. thumbnail при этом сохраняет пропорции, то беру его.

    def resize(self, width, height):
        with Image.open(self.image) as im:
            new_image = im.copy()
            new_image.thumbnail((width, height), Image.LANCZOS)
            buffer = BytesIO()
            new_image.save(fp=buffer, format="PNG")
            self.resized_image.save(
                (self.name + "_resized.png"), ContentFile(buffer.getvalue()))
            # return ContentFile(buffer.getvalue())

    def __str__(self):
        return self.name


# Если картинка не загружена, обращаемся к заданному url
@receiver(pre_save, sender=UserFile)
def download(sender, instance, **kwargs):
    if not instance.image:
        image_variable = request.urlopen(instance.url_variable)
        instance.image.save("downloaded.jpg",
                            ContentFile(image_variable.read()))


# Генерирую имена изображении из их id
@receiver(post_save, sender=UserFile)
def set_name(sender, instance, **kwargs):
    if not instance.name:
        instance.name = "Example" + str(instance.id)
        instance.save()
