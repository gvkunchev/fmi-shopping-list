from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound, JsonResponse
from .models import ShoppingList, ShoppingItem
from .forms import AddShoppingItemForm, AddShoppingListForm

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
        'id': shopping_list.pk,
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


@login_required(login_url='/login')
def remove_item(request):
    """Remove an item."""
    try:
        item = ShoppingItem.objects.get(pk=request.GET['id'])
        # Ensure that a user can't touch other people's stuff
        if item.shopping_list.owner != request.user:
            return HttpResponseNotFound('Invalid link.')
    except (KeyError, ShoppingItem.DoesNotExist):
        return HttpResponseNotFound('Invalid link.')
    item.delete()
    return JsonResponse({'state': 'removed'})


@login_required(login_url='/login')
def add_item(request):
    """Add an item."""
    try:
        name = request.POST['name']
        quantity = request.POST['quantity']
        shopping_list_id = int(request.POST['shopping_list'])
        shopping_list = ShoppingList.objects.get(pk=shopping_list_id)
        # Ensure that a user can't touch other people's stuff
        if shopping_list.owner != request.user:
            return HttpResponseNotFound('Invalid link.')
    except (KeyError, ValueError, ShoppingList.DoesNotExist):
        return HttpResponseNotFound('Invalid link.')
    form = AddShoppingItemForm({'name': name,
                                'quantity': quantity,
                                'shopping_list': shopping_list})
    if form.is_valid():
        form.save()
    return redirect(f'/shopping_list?id={shopping_list_id}')


@login_required(login_url='/login')
def add_list(request):
    """Add a shipping list."""
    try:
        name = request.POST['name']
    except KeyError:
        return HttpResponseNotFound('Invalid link.')
    form = AddShoppingListForm({'name': name,
                                'owner': request.user})
    if form.is_valid():
        form.save()
    return redirect(index)
