from django.shortcuts import render


def pet_add_page(request):
    return render(request, 'pets/pet-add-page.html')


def pet_detail_page(request, pk):
    return render(request, 'pets/pet-details-page.html')


def pet_delete_page(request, pk):
    return render(request, 'pets/pet-delete-page.html')


def pet_edit_page(request, pk):
    return render(request, 'pets/pet-edit-page.html')


