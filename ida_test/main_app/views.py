from django.shortcuts import render, redirect

from PIL import Image
from io import BytesIO

from .models import *
from .forms import UserFileForm, NewSizeForm


def files_list(request):
    files_list = UserFile.objects.all()
    base = True
    return render(request, 'main_app/file_list.html', {'files_list': files_list, 'base': base})


def image_detail(request, pk):
    show_image = False
    # так как второе изображение я все равно сохраняю,
    # то буду показывать результат только после отправки формы
    instance = UserFile.objects.get(pk=pk)

    if request.method == "POST":
        show_image = True
        sizes_form = NewSizeForm(request.POST)
        print(sizes_form.is_valid())
        if sizes_form.is_valid():
            cd = sizes_form.cleaned_data
            if not cd.get('width'):
                cd['width'] = cd['height']
            elif not cd.get('height'):
                cd['height'] = cd['width']
            instance.resize(cd['width'], cd['height'])
            # image_field = instance.resized_image
            # img_name = instance.name + "_resized.png"
            # pillow_image = instance.resize(cd['width'], cd['height'])
            # image_field.save(img_name, InMemoryUploadedFile(
            #     pillow_image, None, img_name, 'image/jpeg', pillow_image.tell, None))

    else:

        sizes_form = NewSizeForm()

    return render(request, 'main_app/image_detail.html',
                  {'sizes_form': sizes_form, 'instance': instance, "show_image": show_image})


def upload(request):
    if request.method == "POST":
        upload_form = UserFileForm(request.POST, request.FILES)
        if upload_form.is_valid():
            new_image = upload_form.save()
            return redirect(new_image)

    else:
        upload_form = UserFileForm()
    return render(request, 'main_app/upload.html', {'upload_form': upload_form})
