from rest_framework import serializers
from .models import Construction, Advantage, Flat, ConstructionImage
from ..news_blog.serializers import PostListSerializer


class AdvantageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advantage
        exclude = ('id', 'construction')


class ConstructionImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConstructionImage
        fields = ('image',)

    def _get_image_url(self, obj):
        if obj.image:
            url = obj.image.url
            requests = self.context.get("request")
            if requests is not None:
                url = requests.build_absolute_uri(url)
        else:
            url = ""
        return url

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = self._get_image_url(instance)
        return representation


class ConstructionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Construction
        fields = ('id', 'title', 'main_picture', 'offer', 'street_address', 'cost_per_square_meter', 'min_price')


class ConstructionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Construction
        exclude = ('id', 'offer', 'cost_per_square_meter')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['advantages'] = AdvantageSerializer(instance.advantage_of_construction.all(), many=True).data
        representation['news'] = PostListSerializer(instance.post_construction.all(), many=True).data
        representation['images'] = ConstructionImageSerializer(ConstructionImage.objects.filter(construction=instance.id),
                                                               many=True).data
        representation['flats'] = FlatListSerializer(instance.layout.all(), many=True).data
        representation['posts'] = PostListSerializer(instance.post_construction.all(), many=True).data
        return representation


class FlatListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flat
        fields = ('id', 'layout_photo',)


class FlatDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flat
        exclude = ('id',)
