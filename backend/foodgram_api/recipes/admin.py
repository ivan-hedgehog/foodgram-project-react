from django.contrib import admin

from .models import Recipe, Ingredient, Tag, IngredientRecipe, TagRecipe

admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Tag)
admin.site.register(IngredientRecipe)
admin.site.register(TagRecipe)


class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'color', 'colored_name')


