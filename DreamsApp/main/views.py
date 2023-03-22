from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from main.models import Dream
from main.serializers import DreamSerializer

#HTTP GET /v1/id/{id}
class ListDreambyID(APIView):
    def get_object(self, id):
        """
        View to get an user just by id
        """
        try:
            return Dream.objects.get(id=id)
        except Dream.DoesNotExist:
            return Http404

    def get(self, request, id, format =None):
        dream = self.get_object(id)
        serializer = DreamSerializer(dream)
        return Response(dream)

#HTTP GET /v1/quote/contain_string

#HTTP GET /v1/before_date/{date}

#HTTP GET /v1/after_date/{date}


#POST(id, User, current date, quote)
#HTTP POST /v1/new_entry (data will be defined in the content body)

#DELETE(Do based off primary key id)
#HTTP POST /v1/delete_entry (data will be defined in the content body)