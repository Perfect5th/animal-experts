from rest_framework import serializers

from expert_search.models import Expert, FieldCategory


class FieldCategorySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='fieldcategory-detail',
        lookup_field='code')

    class Meta:
        model = FieldCategory
        fields = ('url', 'name')


class ExpertSerializer(serializers.HyperlinkedModelSerializer):
    fields = FieldCategorySerializer(many=True)

    class Meta:
        model = Expert
        fields = ('url', 'title', 'first_name', 'last_name', 'affiliation',
            'subjects', 'fields', 'website', 'description')
