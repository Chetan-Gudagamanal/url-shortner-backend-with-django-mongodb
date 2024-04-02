from rest_framework import serializers


# class CommentSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     content = serializers.CharField(max_length=200)
#     created = serializers.DateTimeField()

class UrlSerializer(serializers.Serializer):
    long_url = serializers.CharField(max_length=200)
    short_url_code = serializers.CharField(max_length=200)
