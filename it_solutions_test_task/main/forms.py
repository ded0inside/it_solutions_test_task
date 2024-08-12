from .models import Subtitles
from django.forms import ModelForm, TextInput, NumberInput


class SubtitlesForm(ModelForm):
    class Meta:
        model = Subtitles
        fields = ['text', 'font_size', 'rf', 'gf', 'bf', 'rb', 'gb', 'bb']

        widgets = {
            "text": TextInput(attrs={
                "id": "text",
                "placeholder": "Введите текст"
            }),
            'font_size': NumberInput(attrs={
                "id": "font_size"
            }),
            'rf': NumberInput(attrs={
                "id": "rf"
            }),
            'gf': NumberInput(attrs={
                "id": "gf"
            }),
            'bf': NumberInput(attrs={
                "id": "bf"
            }),
            'rb': NumberInput(attrs={
                "id": "rb"
            }),
            'gb': NumberInput(attrs={
                "id": "gb"
            }),
            'bb': NumberInput(attrs={
                "id": "bb"
            }),
        }