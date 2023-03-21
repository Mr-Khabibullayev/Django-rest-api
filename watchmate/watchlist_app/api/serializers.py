from rest_framework import serializers
from watchlist_app.models import WatchList,StreamPlatform, Reviews


class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Reviews    
        fields = '__all__'                


class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True,read_only=True)
    
    class Meta:
        model = WatchList
        fields = '__all__'
        

class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True,read_only=True)
    
    class Meta:
        model = StreamPlatform
        fields = '__all__'
        
        
        
        
        
# def name_lenth(value):
#     if len(value) < 2:
#         raise serializers.ValidationError('Name is to short')

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_lenth])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self,validated_data):
#         return Movie.objects.create(**validated_data)
        
#     def update(self,instance, validate_data):
#         instance.name = validate_data.get('name',instance.name)
#         instance.description = validate_data.get('description', instance.description)
#         instance.active = validate_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError('Title and Description should be defferent!')
#         else:
#             return data
        
#         return 
    
#     def validate_name(self,value):
#         if len(value) < 2:
#             raise serializers.ValidationError('Name is too short')
#         else:
#             return value
            