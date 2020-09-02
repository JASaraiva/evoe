from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from todolist.list.models import List
from todolist.list.api.serializers import ListSerializer

class ListViewSet(ModelViewSet):

    permission_classes = [IsAuthenticated] 
    authentication_classes = [TokenAuthentication] 

    #queryset = List.objects.all()
    serializer_class = ListSerializer

    def get_queryset(self):
        userid = self.request.user.id
        return List.objects.filter(user = userid)
      


    def create(self, request):

        item = {"item": request.data["item"],
           "checked": request.data["checked"],
           "user": request.user.id,
        }
        

        serializer = self.get_serializer(data=item)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)