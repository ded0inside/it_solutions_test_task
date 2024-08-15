from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import ImageSequenceClip
import numpy as np
import os

# Настройки
TEXT = "Длинный текст супер длинный текст"
FONT_SIZE = 70
IMAGE_WIDTH = 100
IMAGE_HEIGHT = 100
FPS = 24  # Частота кадров


# Создание кадра для видео бегущей строкой
def create_frame(text, offset, background_color, font_color, font_size):
    '''Создает кадр с позиционированным текстом'''
    global IMAGE_WIDTH, IMAGE_HEIGHT

    # Создание пустого изображение
    image = Image.new('RGB', (IMAGE_WIDTH, IMAGE_HEIGHT), background_color)
    draw = ImageDraw.Draw(image)

    # Настройка шрифт
    # font = ImageFont.truetype("Arial", font_size)  # Для обычного запуска раскоментируете эту строчку и закоментируите следущую
    font = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf", font_size)  # Нужно для колаба
    
    # Вычисление ширины текста
    bbox = draw.textbbox((0, 0), text, font=font)
    # text_width = bbox[2] - bbox[0]  # Пока не используется, пофиксим в будущем
    text_height = bbox[3] - bbox[1]

    # Позиция якоря для текста
    x = IMAGE_WIDTH / 2 + offset
    y = IMAGE_HEIGHT / 2 - text_height / 2

    # Отрисовка текста на изображении
    draw.text((x, y), text, font=font, fill=font_color)

    return np.array(image)


def create_subtitle_video(text, font="Arial", font_size=FONT_SIZE, font_color=(255, 255, 255),
                          background_color=(0, 0, 0)):
    '''Создает видео с бегущей строкой, возвращает путь до файла в папке media'''
    global IMAGE_WIDTH, IMAGE_HEIGHT, FPS

    # Настройка шрифт
    # font = ImageFont.truetype("Arial", font_size)  # Для обычного запуска раскоментируете эту строчку и закоментируите следущую
    font = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf", font_size)  # Нужно для колаба
                              
    # Создание одного кадра для получения ширины текста
    bbox = ImageDraw.Draw(Image.new('RGB', (IMAGE_WIDTH, IMAGE_HEIGHT))).textbbox((0, 0), text,
                                                                                  font=font)
    # Создание служебных переменных
    frames = []  # Массив кадров для видео
    # offset = IMAGE_WIDTH  # Начальная позиция текста за пределами экрана
    offset = 0  # Начальная позиция текста если нужно сразу выводить текст на экран
    text_width = bbox[2] - bbox[0]  # Длина текста в пикселях
    text_speed = (text_width + IMAGE_WIDTH) // (FPS * 3)  # Скорость смещения (пикселей/кадр), чтобы уложиться в 3с

    while True:
        frame = create_frame(text, offset, background_color, font_color, font_size)
        frames.append(frame)
        offset -= text_speed  # Изменение смещения текста

        if -offset >= text_width:  # Выходим из цикла, когда весь текст отрисован
            break

    # Путь для записи файла
    output_path = os.path.join("media", "subtitle_video.mp4")

    # Создание видео из кадров
    clip = ImageSequenceClip(frames, fps=FPS)
    clip.write_videofile(output_path, codec='libx264')

    return output_path


if __name__ == '__main__':
    create_subtitle_video(TEXT)
    print("Видео успешно создано!")
