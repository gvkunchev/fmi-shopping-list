from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound, JsonResponse
from base.models import ShoppingList, ShoppingItem
from base.forms import (AddShoppingItemForm, AddShoppingListForm,
                        RegisterUserForm)
from .view_decorators import can_view_item


@login_required(login_url='/login')
def index(request):
    """Welcome page."""
    context = {
        'shopping_lists': ShoppingList.objects.filter(owner=request.user),
        'username': request.user.username
    }
    return render(request, 'index.html', context)


@can_view_item(ShoppingList)
@login_required(login_url='/login')
def shopping_list(request):
    """Individual shopping list page."""
    shopping_list = ShoppingList.objects.get(pk=request.GET['id'])
    context = {
        'name': shopping_list.name,
        'id': shopping_list.pk,
        'items': shopping_list.items.all()
    }
    return render(request, 'shopping_list.html', context)


@can_view_item(ShoppingItem)
@login_required(login_url='/login')
def toggle_item(request):
    """Toggle between bought states of an item."""
    item = ShoppingItem.objects.get(pk=request.POST['id'])
    try:
        state = request.POST['state'] == '1'
    except KeyError:
        return HttpResponseNotFound('Invalid link.')
    item.bought = state
    item.save()
    return JsonResponse({'state': item.bought})


@can_view_item(ShoppingItem)
@login_required(login_url='/login')
def remove_item(request):
    """Remove an item."""
    item = ShoppingItem.objects.get(pk=request.POST['id'])
    item.delete()
    return JsonResponse({'state': 'removed'})


@can_view_item(ShoppingList)
@login_required(login_url='/login')
def add_item(request):
    """Add an item."""
    try:
        name = request.POST['name']
        quantity = request.POST['quantity']
    except KeyError:
        return HttpResponseNotFound('Invalid link.')
    shopping_list_id = int(request.POST['id'])
    shopping_list = ShoppingList.objects.get(pk=shopping_list_id)
    form = AddShoppingItemForm({'name': name,
                                'quantity': quantity,
                                'shopping_list': shopping_list})
    if form.is_valid():
        form.save()
    return redirect(f'/shopping_list?id={shopping_list_id}')


@login_required(login_url='/login')
def add_list(request):
    """Add a shopping list."""
    try:
        name = request.POST['name']
    except KeyError:
        return HttpResponseNotFound('Invalid link.')
    form = AddShoppingListForm({'name': name,
                                'owner': request.user})
    if form.is_valid():
        form.save()
    return redirect(index)


@can_view_item(ShoppingList)
@login_required(login_url='/login')
def remove_list(request):
    """Remove a shopping list."""
    shopping_list = ShoppingList.objects.get(pk=request.POST['id'])
    shopping_list.delete()
    return JsonResponse({'state': 'removed'})


def register(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(index)
    else:
        form = RegisterUserForm()
    context = {
        'form': form
    }
    return render(request, 'registration/register.html', context)
