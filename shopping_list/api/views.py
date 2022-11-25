from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import ShoppingList
from django.contrib.auth import authenticate
from .serializers import ShoppingListSerializer

@api_view(['GET',])
def get_shopping_lists(request):
    """Return list of shopping lists for a user."""
    serializer = ShoppingListSerializer(ShoppingList.objects.all(), many=True)
    return Response(serializer.data)


@api_view(['POST',])
def authenticate_user(request):
    user = authenticate(username=request.data['username'],
                        password=request.data['password'])
    if user is not None:
        return Response({'success': user.pk})
    else:
        return Response({'error': -1})
