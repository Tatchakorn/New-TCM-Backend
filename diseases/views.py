from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .models import Diseases
from .serializers import DiseasesSerializer

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100



class DiseasesViewset(viewsets.ModelViewSet):
    pagination_class = StandardResultsSetPagination
    queryset = Diseases.objects.all()
    serializer_class = DiseasesSerializer
