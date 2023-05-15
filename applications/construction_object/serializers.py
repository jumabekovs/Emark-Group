from rest_framework import serializers
from .models import Construction, Advantage, Flat, ConstructionImage, Feature, Infrastructure, Block, FlatImages, \
    PriceList, Room
from ..news_blog.serializers import PostListSerializer


class InfrastructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Infrastructure
        exclude = ('id', )


class FeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = '__all__'


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


class PriceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceList
        fields = '__all__'


class ConstructionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Construction
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['advantages'] = AdvantageSerializer(instance.advantage_of_construction.all(), many=True).data
        representation['news'] = PostListSerializer(instance.post_construction.all(), many=True).data
        representation['images'] = ConstructionImageSerializer(ConstructionImage.objects.filter(construction=instance.id),
                                                               many=True).data
        representation['flats'] = FlatListSerializer(instance.layout.all(), many=True).data
        representation['features'] = FeaturesSerializer(instance.features.all(), many=True).data
        representation['district'] = str(instance.district.title)
        representation['construction_completion_year'] = str(instance.construction_completion_year.year)
        representation['posts'] = PostListSerializer(instance.post_construction.all(), many=True).data
        representation['infrastructure'] = InfrastructureSerializer(instance.infrasrtucture_nearby.all(), many=True).data
        representation['price_list'] = PriceListSerializer(instance.price_list.all(), many=True).data
        return representation


class ConstructionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Construction
        fields = "__all__"

    def get_count(self, obj):
        return obj.filter(selling_status='')


class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['construction'] = str(instance.construction.title)
        return representation


class FlatListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flat
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['block'] = str(instance.block)
        representation['block_image'] = str(instance.layout_photo)
        representation['side'] = str(instance.block.sides)
        return representation


class FlatImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlatImages
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


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        exclude = ("id", "flat")


class FlatDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flat
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['rooms'] = RoomSerializer(instance.room.all(), many=True).data
        representation['images'] = FlatImageSerializer(instance.flat_images.all(), many=True).data
        representation['block'] = str(instance.block)
        representation['side'] = str(instance.block.sides)
        representation['block_image'] = str(instance.block.plan_model)
        representation['block'] = BlockSerializer(instance.block).data
        return representation

