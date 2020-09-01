from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from todolist.list.models import List
from todolist.list.api.serializers import ListSerializer

class ListViewSet(ModelViewSet):

    permission_classes = [IsAuthenticated] 
    authentication_classes = [TokenAuthentication] 

    queryset = List.objects.all()
    serializer_class = ListSerializer