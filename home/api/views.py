from rest_framework import generics
from home.models import Subscriber
from .serializers import SubscriberSerializer


class SubscriberAPIView(generics.CreateAPIView):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer