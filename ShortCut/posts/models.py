from django.db import models
from django.contrib.auth import get_user_model
from core.models import CreatedModel
from django.core.validators import FileExtensionValidator

User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        max_length=200
    )
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Post(CreatedModel):
    title = models.TextField(
        verbose_name='Название фильма',
        help_text='Текст длиной до 500 символов',
        blank=False
    )
    description = models.TextField(
        verbose_name='Описание вашего фильма',
        help_text='Текст длиной до 500 символов',
        blank=False
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    group = models.ForeignKey(
        Group,
        verbose_name='Плейлист',
        blank=True, null=True,
        on_delete=models.SET_NULL,
        related_name='posts',
        help_text='Укажите название плейлиста'
    )
    image = models.ImageField(
        verbose_name='Картинка',
        upload_to='image/',
        blank=False,
        help_text='Загрузите сюда вашу картинку'
    )
    video = models.FileField(
        upload_to='video/',
        blank=False,
        validators=[FileExtensionValidator(allowed_extensions=['mp4'])]
    )

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.title


class Comment(CreatedModel):
    text = models.TextField(
        verbose_name='Текст комментария',
        help_text='Текст вашего комментария'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    def __str__(self):
        return self.text[:15]


class Follow(CreatedModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following'
    )

