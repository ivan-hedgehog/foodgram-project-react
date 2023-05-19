
from django.core.management.base import BaseCommand
import json
from recipes.models import Ingredient


class Command(BaseCommand):
    def handle(self, *args, **options):

        with open('ingredients.json', 'rb') as f:
            data = json.load(f)

            for x, y in data.items():
                print(x)
                print(y)
                ingredient = Ingredient()
                ingredient.name = x
                ingredient.measurement_unit = y
                ingredient.save()
                # s.genres.add(g)
        print('finished')
