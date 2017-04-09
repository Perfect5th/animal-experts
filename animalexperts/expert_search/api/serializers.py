from rest_framework import serializers

from expert_search.models import Expert, FieldCategory


class ExpertSerializer(serializers.HyperlinkedModelSerializer):
    fields = serializers.HyperlinkedRelatedField(allow_empty=True, many=True,
        lookup_field='code', queryset=FieldCategory.objects.all(),
        view_name='fieldcategory-detail')
    
    class Meta:
        model = Expert
        fields = ('url', 'title', 'first_name', 'last_name', 'affiliation',
            'subjects', 'fields', 'email', 'website', 'description')


class FieldCategorySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='fieldcategory-detail',
        lookup_field='code')
    
    class Meta:
        model = FieldCategory
        fields = ('url', 'name')
