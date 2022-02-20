from rest_framework import serializers
from home.models import Subscriber


class SubscriberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscriber
        fields =(
            'id',
            'email',
            'created_at'
        )