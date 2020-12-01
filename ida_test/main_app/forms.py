from django import forms
from django.forms import ValidationError

from .models import UserFile


class UserFileForm(forms.ModelForm):
    class Meta:
        model = UserFile
        fields = ['url_variable', 'image']

    def clean(self):
        cleaned_data = super().clean()
        url_field = cleaned_data.get('url_variable')
        image_field = cleaned_data.get('image')

        if not image_field and not url_field:

            raise ValidationError(
                'Должно быть заполнено хотя бы одно поле')
        elif image_field and url_field:

            raise ValidationError('Должно быть заполнено только одно поле')


class NewSizeForm(forms.Form):
    width = forms.IntegerField(min_value=1, required=False)
    height = forms.IntegerField(min_value=1, required=False)

    def clean(self):
        cleaned_data = super().clean()

        width_field = cleaned_data.get('width')
        height_field = cleaned_data.get('height')
        if not width_field and not height_field:
            raise ValidationError('Заполните хотя бы одно поле')
