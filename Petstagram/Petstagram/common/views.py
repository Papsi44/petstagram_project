from django.shortcuts import render

from Petstagram.photos.models import Photo


def home_page(request):
    all_photos = Photo.objects.all()
    context = {'all_photos': all_photos}
    return render(request, 'common/home-page.html', context)

