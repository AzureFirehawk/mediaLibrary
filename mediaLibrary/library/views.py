from django.shortcuts import render, get_object_or_404, redirect
from .models import MediaItem
from .forms import MediaItemForm

def media_list(request):
    items = MediaItem.objects.all().order_by('-created_at')

    status_filter = request.GET.get('status')
    type_filter = request.GET.get('type')

    if status_filter:
        items = items.filter(status=status_filter)

    if type_filter:
        items = items.filter(type=type_filter)

    return render(request, 'library/media_list.html', {
        'items': items,
        'status_filter': status_filter,
        'type_filter': type_filter,
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

def media_edit(request, pk):
    item = get_object_or_404(MediaItem, pk=pk)

    if request.method == 'POST':
        form = MediaItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('library:media_detail', pk=item.pk)
    else:
        form = MediaItemForm(instance=item)

    return render(request, 'library/media_form.html', {
        'form': form,
        'item': item
    })