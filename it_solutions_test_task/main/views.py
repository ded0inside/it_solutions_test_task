from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse
from .models import Subtitles
from .forms import SubtitlesForm
from .subtitle_creator import create_subtitle_video


# Create your views here.
def index(request):
    error = '' # Обработка ошибки

    if request.method == 'POST':
        form = SubtitlesForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)  # Необходимо чтобы достать данные из формы

            # Данные для настройки видео
            text = form.cleaned_data['text']
            font_size = form.cleaned_data['font_size']
            font_color = (form.cleaned_data['rf'], form.cleaned_data['gf'], form.cleaned_data['bf'])
            background_color = (form.cleaned_data['rb'], form.cleaned_data['gb'], form.cleaned_data['bb'])

            video_path = create_subtitle_video(text, font_size=font_size, font_color=font_color,
                                               background_color=background_color)
            instance.save()  # Созранение в БД

            # Сохранение файла на стороне пользователя
            with open(video_path, 'rb') as video:
                response = HttpResponse(video.read(), content_type='video/mp4')
                response['Content-Disposition'] = f'attachment; filename="subtitle_video.mp4"'

                return response
        else:
            error = 'Something went wrong!'
    else:
        subtitles = Subtitles.objects.all().order_by('-id')[:5]
        form = SubtitlesForm()

    data = {
        "subtitles": subtitles,
        "form": form,
        "error": error,
    }
    return render(request, 'main/index.html', data)

