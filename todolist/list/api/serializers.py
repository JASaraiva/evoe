from rest_framework.serializers import ModelSerializer
from todolist.list.models import List

class ListSerializer(ModelSerializer):
    class Meta:
        model= List
        fields= ['item', 'status', 'user']
