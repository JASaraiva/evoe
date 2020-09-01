from rest_framework.viewsets import ModelViewSet
from todolist.list.models import List
from todolist.list.api.serializers import ListSerializer

class ListViewSet(ModelViewSet):

    queryset = List.objects.all()
    serializer_class = ListSerializer