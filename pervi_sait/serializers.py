

from rest_framework.serializers import ModelSerializer


from pervi_sait.models import Wheels


class WheelsSerializer(ModelSerializer):
    class Meta:
        model = Wheels
        fields = '__all__'
