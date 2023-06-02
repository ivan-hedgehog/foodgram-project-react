from django.conf import settings
from django.core.validators import RegexValidator
from django.db import models
from users.models import User


class Ingredient(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Название ингредиента',
        db_index=True,
    )
    measurement_unit = models.CharField(
        max_length=80,
        verbose_name='Еденица измерения',
    )

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        ordering = ('name',)

    def __str__(self):
        return f'{self.id}, {self.name}'


class Tag(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название тега',
        unique=True,
    )
    slug = models.SlugField(
        max_length=150,
        unique=True,
        verbose_name='Идентификатор тега',
        db_index=True,
        null=True,
    )
    color = models.CharField(
        max_length=7,
        verbose_name='Цвет тега',
        default='#ffffff',
        unique=True,
        validators=[RegexValidator(r'^#[A-Fa-f0-9]{6}$')],
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ('name',)

    def __str__(self):
        return self.slug


class Recipe(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Название',
    )
    text = models.TextField(
        verbose_name='Текстовое описание',
        max_length=512,
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор',
    )
    image = models.ImageField(
        'Изображение',
        upload_to='recipes/',
        null=True,
        default=None,
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        through='IngredientRecipe',
        verbose_name='Ингредиенты',
    )
    tag = models.ManyToManyField(
        Tag,
        through='TagRecipe',
        verbose_name='Теги',
    )
    cooking_time = models.PositiveSmallIntegerField(
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
        related_name='ingredients',
        verbose_name='Название ингредиента',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Название рецепта',
    )
    amount = models.PositiveSmallIntegerField(
        verbose_name='Количество ингредиента',
    )

    class Meta:
        verbose_name = 'количество ингредиента'
        verbose_name_plural = 'количество ингредиентов'
        ordering = ('amount',)
        constraints = [
            models.UniqueConstraint(
                fields=['recipe', 'ingredient'],
                name='unique_ingredient_for_recipe',
            )
        ]

    def __str__(self):
        return (f'{self.recipe.name}: '
                f'{self.ingredient.name} - '
                f'{self.amount} '
                f'{self.ingredient.measurement_unit}')


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
        constraints = [
            models.UniqueConstraint(
                fields=['recipe', 'tag'], name='unique_tag_for_recipe'
            )
        ]

    def __str__(self):
        return f'{self.tag} принадлежит рецепту {self.recipe}'


class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        related_name='favorites',
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
    )
    recipe = models.ForeignKey(
        Recipe,
        related_name='favorites',
        on_delete=models.CASCADE,
        verbose_name='Рецепт'
    )

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные рецепты'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'recipe'], name='unique_favorite_recipe'
            )
        ]

    def __str__(self):
        return f'{self.user} - {self.recipe}'


class ShoppingCart(models.Model):
    user = models.ForeignKey(
        User,
        related_name='shoppings',
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
    )
    recipe = models.ForeignKey(
        Recipe,
        related_name='shoppings',
        on_delete=models.CASCADE,
        verbose_name='Рецепт'
    )

    class Meta:
        verbose_name = 'Список покупок'
        verbose_name_plural = 'Списки покупок'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'recipe'], name='unique_shopping_cart'
            )
        ]

    def __str__(self):
        return f'{self.user} - {self.recipe}'
