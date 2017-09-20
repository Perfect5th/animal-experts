from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.http import Http404

from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from expert_search.models import Expert, FieldCategory

from .serializers import ExpertSerializer, FieldCategorySerializer


class ExpertList(generics.ListCreateAPIView):
    serializer_class = ExpertSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        queryset = Expert.objects.all()
        search_term = self.request.query_params.get('q')
        if search_term:
            vector = SearchVector('subjects') + SearchVector('fields__name')
            query = SearchQuery(search_term)
            queryset = queryset.annotate(
                rank=SearchRank(vector, query)).order_by('-rank')
        else:
            queryset = queryset.order_by('pk')
        return queryset


class ExpertDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expert.objects.all()
    serializer_class = ExpertSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class FieldCategoryList(generics.ListCreateAPIView):
    queryset = FieldCategory.objects.all()
    serializer_class = FieldCategorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class FieldCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FieldCategory.objects.all()
    serializer_class = FieldCategorySerializer
    lookup_field = 'code'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'experts': reverse('expert-list', request=request, format=format),
        'fields': reverse('fieldcategory-list', request=request, format=format)
    })
