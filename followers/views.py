from rest_framework import generics, permissions
from drf_ci.permissions import IsOwnerOrReadOnly
from followers.models import Follower
from followers.serializers import FollowerSerializer

class FollowerList(generics.ListCreateAPIView):
    """
    List Followers or start following if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class FollowerDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a Follow or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()