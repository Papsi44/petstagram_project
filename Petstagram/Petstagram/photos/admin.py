from django.contrib import admin

from Petstagram.photos.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_of_publication', 'get_tagged_pets')

    @staticmethod
    def get_tagged_pets(obj):
        return ", ".join(pet.name for pet in obj.tagged_pets.all())
