from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django_filters import rest_framework as filters
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
        return Response(serializer.data)

#HTTP GET/v1/allquotes
#HTTP GET /v1/quote/contain_string

class GetAllQuotes(generics.ListAPIView):
    serializer_class = DreamSerializer
    def get_queryset(self):
        queryset = Dream.objects.all()
        contains_string = self.request.query_params.get('contains_string')
        if contains_string is not None:
            queryset = queryset.filter(quote__contains=contains_string)
        return queryset

#HTTP GET /v1/before_date/{date}
#HTTP GET /v1/after_date/{date}
class GetDateFilter(filters.FilterSet):
    date = filters.DateFromToRangeFilter()
    class Meta: 
        model = Dream
        fields =['date']

class ListDreamByDate(generics.ListAPIView):
    queryset = Dream.objects.all()
    serializer_class = DreamSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = GetDateFilter


#POST(id, User, current date, quote)
#HTTP POST /v1/new_entry (data will be defined in the content body)

#DELETE(Do based off primary key id)
#HTTP POST /v1/delete_entry (data will be defined in the content body)