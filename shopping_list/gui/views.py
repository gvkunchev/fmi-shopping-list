from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ShoppingList


@login_required(login_url='/login')
def index(request):
    """Welcome page."""
    context = {
        'shopping_lists': ShoppingList.objects.filter(owner=request.user)
    }
    return render(request, 'index.html', context)
