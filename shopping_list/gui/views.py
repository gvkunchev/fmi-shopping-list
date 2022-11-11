from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ShoppingList, ShoppingItem
from django.http import HttpResponseNotFound, JsonResponse


@login_required(login_url='/login')
def index(request):
    """Welcome page."""
    context = {
        'shopping_lists': ShoppingList.objects.filter(owner=request.user),
        'username': request.user.first_name or request.user.email
    }
    return render(request, 'index.html', context)


@login_required(login_url='/login')
def shopping_list(request):
    """Individual shopping list page."""
    try:
        shopping_list = ShoppingList.objects.get(pk=request.GET['id'])
    except (KeyError, ShoppingList.DoesNotExist):
        return HttpResponseNotFound('Invalid link. No ID found.')
    context = {
        'name': shopping_list.name,
        'items': shopping_list.items.all()
    }
    return render(request, 'shopping_list.html', context)


@login_required(login_url='/login')
def toggle_item(request):
    """Toggle between bought states of an item."""
    try:
        item = ShoppingItem.objects.get(pk=request.GET['id'])
        state = request.GET['state'] == '1'
        # Ensure that a user can't touch other people's stuff
        if item.shopping_list.owner != request.user:
            return HttpResponseNotFound('Invalid link.')
    except (KeyError, ShoppingItem.DoesNotExist):
        return HttpResponseNotFound('Invalid link.')
    item.bought = state
    item.save()
    return JsonResponse({'state': item.bought})
