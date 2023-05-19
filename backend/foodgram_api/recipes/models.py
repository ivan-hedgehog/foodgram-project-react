from django.contrib import admin
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.html import format_html

User = get_user_model()


class Ingredient(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Название ингредиента',
    )
    measurement_unit = models.CharField(
        max_length=50,
        verbose_name='Еденица измерения',
    )

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название тега',
        unique=True,
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name='Идентификатор тега',
    )
    color = models.CharField(
        max_length=7,
        verbose_name='Цвет тега',
        default='#ffffff',
        unique=True,
    )

    def colored_name(self):
        return format_html(
            '<span style="color: #{};">{}</span>',
            self.color,
        )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ('name',)

    def __str__(self):
        return self.title


class Recipe(models.Model):
    name = models.CharField(
        max_length=256,
        db_index=True,
        verbose_name='Название',
    )
    text = models.TextField(
        verbose_name='Текстовое описание',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор',
    )
    image = models.ImageField(
        'Изображение',
        upload_to='recipes/',
    )
    ingredient = models.ManyToManyField(
        Ingredient,
        # through='IngredientRecipe',
        # blank=True,
        verbose_name='Ингредиент',
    )
    tag = models.ManyToManyField(
        Tag,
        # through='TagRecipe',
        # blank=True,
        verbose_name='Тег',
    )
    cooking_time = models.SmallIntegerField(
        'Время приготовления (в минутах)',
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name


class IngredientRecipe(models.Model):
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        verbose_name='Название ингредиента',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Название рецепта',
    )
    quantity = models.SmallIntegerField(
        verbose_name='Количество ингредиента',
    )

    class Meta:
        verbose_name = 'количество ингредиента'
        verbose_name_plural = 'количество ингредиентов'
        ordering = ('quantity',)

    def __str__(self):
        return self.quantity


class TagRecipe(models.Model):
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Тег рецепта'
        verbose_name_plural = 'Теги рецептов'
        ordering = ('recipe',)

    def __str__(self):
        return f'{self.tag} принадлежит рецепту {self.recipe}'
