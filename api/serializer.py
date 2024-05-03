from rest_framework.serializers import ModelSerializer
from app.models import Movie
class MovieSerializer(ModelSerializer):
    class Meta:
        model=Movie
        fields=("id","image","name","time","release","vedioadjactive","syujeti")
class MovieDetailSerializer(ModelSerializer):
    class Meta:
        model=Movie
        fields=("__all__")
