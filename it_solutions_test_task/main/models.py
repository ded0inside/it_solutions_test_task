from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Subtitles(models.Model):
    # Можно было бы использовать и TextField, но большие тексты слишком быстро "бегают" из-за ограничения в 3 с
    text = models.CharField('user_text',
                            max_length=50)  # Эксперементально можно вычислить, на сколько длинный текст можно допускать
    font_size = models.IntegerField('font_size', default=40, validators=[MinValueValidator(1), MaxValueValidator(100)])
    rf = models.IntegerField('red_f', validators=[MinValueValidator(0), MaxValueValidator(255)], default=0)
    gf = models.IntegerField('green_f', validators=[MinValueValidator(0), MaxValueValidator(255)], default=0)
    bf = models.IntegerField('blue_f', validators=[MinValueValidator(0), MaxValueValidator(255)], default=0)
    rb = models.IntegerField('red_b', validators=[MinValueValidator(0), MaxValueValidator(255)], default=255)
    gb = models.IntegerField('green_b', validators=[MinValueValidator(0), MaxValueValidator(255)], default=255)
    bb = models.IntegerField('blue_b', validators=[MinValueValidator(0), MaxValueValidator(255)], default=255)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Subtitle'
        verbose_name_plural = 'Subtitles'
