
from django.db.models import Sum
from recipes.models import IngredientRecipe


def shopping_cart(request):
    text = 'Cписок покупок: \n'

    shopping_cart = IngredientRecipe.objects.filter(
        recipe_id__in=request.user.shoppings.values_list(
            'recipe_id', flat=True
        )
    ).values_list(
        'ingredient__name', 'ingredient__measurement_unit'
    ).annotate(Sum('amount'))

    for index, ingredient in enumerate(sorted(shopping_cart), start=1):
        text += f'{index}. {ingredient[0].capitalize()} ' \
                f'({ingredient[1]}) - {ingredient[2]};\n'

    return text
