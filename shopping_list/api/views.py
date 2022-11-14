from rest_framework.decorators import api_view
from rest_framework.response import Response
from gui.models import ShoppingList


@api_view(['GET',])
def get_shopping_lists(request):
    """Return list of shopping lists for a user."""
    name_list = [x.name for x in ShoppingList.objects.all()]
    return Response({'list': name_list})
