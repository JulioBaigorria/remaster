from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins, viewsets
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from rest_framework_simplejwt.tokens import RefreshToken
from . import serializers
from .models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserListSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return serializers.UserRetrieveSerializer
        if self.action == 'list':
            return serializers.UserListSerializer
        elif self.action == 'create':
            return serializers.UserCreateSerializer
        return self.serializer_class


class LogOutView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            print(refresh_token)
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class LogOutAllView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        tokens = OutstandingToken.objects.filter(user_id=request.user.id)
        print(tokens)
        for token in tokens:
            t, _ = BlacklistedToken.objects.get_or_create(token=token)

        return Response(status=status.HTTP_205_RESET_CONTENT)
