from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ShoppingList
from django.http import HttpResponseNotFound



@login_required(login_url='/login')
def index(request):
    """Welcome page."""
    context = {
        'shopping_lists': ShoppingList.objects.filter(owner=request.user)
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
