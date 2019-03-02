from PIL import Image
from autoslug import AutoSlugField
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse
from django.utils import timezone
from mptt.models import MPTTModel, TreeForeignKey


# Create your models here.
class MainSlider(models.Model):
    image = models.ImageField(null=False, blank=False, upload_to='images_for_slider/', verbose_name=u'Изображение')
    text = models.CharField(max_length=200, null=True, blank=True,
                            verbose_name=u'Основной текст')
    is_visible = models.BooleanField(default=True, verbose_name=u'Показывать объявление?')

    class Meta:
        verbose_name = 'Изображение(слайдер)'
        verbose_name_plural = 'Изображения(слайдер)'

    def __str__(self):
        return self.text

    def save(self, *args, **kwargs):
        super(MainSlider, self).save(*args, **kwargs)
        image = Image.open(self.image)
        size = (1024, 480)
        image = image.resize(size, Image.ANTIALIAS)
        image.save(self.image.path)


class Catalog(MPTTModel):
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children',
                            verbose_name=u'Родительский каталог')
    label = models.CharField(max_length=50, verbose_name=u'Название каталога')
    slug = AutoSlugField(populate_from='label', default='slug', always_update=True, unique=True)
    image = models.ImageField(upload_to='images_for_catalogs/', null=False, blank=False,
                              verbose_name='Картинка для каталога')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлен')
    is_visible = models.BooleanField(default=True, verbose_name=u'Показывать каталог?')

    def __str__(self):
        return self.label

    class Meta:
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталог'

    def get_url(self):
        return reverse("product_list_view", args=(self.slug,))


class Product(models.Model):
    catalog = models.ForeignKey('handicrafts.Catalog', related_name='products', on_delete=models.CASCADE,
                                verbose_name=u'Каталог')
    label = models.CharField(max_length=75, unique=True, null=False, blank=False, verbose_name=u'Название товара')
    slug = AutoSlugField(populate_from='label', default='slug', always_update=True, unique=True)
    price = models.IntegerField(null=True, blank=True, verbose_name=u'Цена')
    description = models.TextField(null=True, blank=True, verbose_name=u'Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлен')
    is_visible = models.BooleanField(default=True, verbose_name=u'Показывать товар?')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.label

    def get_url(self):
        return reverse("product_detail_view", args=(self.catalog.slug, self.slug,))


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE, )
    image = models.ImageField(upload_to='images_for_products/', verbose_name=u'Изображение')
    priority = models.IntegerField(default=5, verbose_name=u'Приоритет показа')
    created_date = models.DateTimeField(default=timezone.now, verbose_name=u'Дата добавления картинки')

    class Meta:
        ordering = ["priority"]
        verbose_name = 'Изображение к товару'
        verbose_name_plural = 'Изображения к товару'
