from django.core.management.base import BaseCommand
import json
import os
from recipes.models import Ingredient


class Command(BaseCommand):
    help = 'Add data to bd'
    
    def handle(self, *args, **options):

        with open('recipes/data/ingredients.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

            for ingredients in data:
                name = ingredients['name']
                measurement_unit = ingredients['measurement_unit']
                Ingredient.objects.create(
                    name=name,
                    measurement_unit=measurement_unit
                )
        print('finished')


# def load_data_from_json(file_path):
#     with open (file_path, 'r', encoding='utf-8') as file:
#         data = json.load(file)
#         for item in data:
#             ingredient = Ingredient.objects.create(
#                 name=item['name'],
#                 measurement_unit=item['measurement_unit'],
#             )

# json_file_path = 'recipes/data/ingredients.json'

# load_data_from_json(json_file_path)

