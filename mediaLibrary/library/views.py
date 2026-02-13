from django.shortcuts import render, get_object_or_404, redirect
from .models import MediaItem
from .forms import MediaItemForm

def media_list(request):
    items = MediaItem.objects.all().order_by('-created_at')
    return render(request, 'library/media_list.html', {
        'items': items
    })

def media_detail(request, pk):
    item = get_object_or_404(MediaItem, pk=pk)
    return render(request, 'library/media_detail.html', {
        'item': item
    })

def media_create(request):
    if request.method == 'POST':
        form = MediaItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('library:media_list')
    else:
        form = MediaItemForm()

    return render(request, 'library/media_form.html', {
        'form': form
    })
