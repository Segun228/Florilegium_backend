from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import User
from .serializers import UserSerializer

class TelegramAuthView(APIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    def post(self, request):
        telegram_id = request.data.get("telegram_id")
        username = request.data.get("username")

        if not telegram_id or not username:
            return Response({"error": "Missing telegram_id or username"}, status=status.HTTP_400_BAD_REQUEST)

        user, created = User.objects.get_or_create(
            telegram_id=telegram_id,
            defaults={"username": username}
        )

        return Response({
            "message": "Authenticated",
            "user_id": user.telegram_id, # type: ignore
            "username": user.username,
            "created": created
        }, status=status.HTTP_200_OK)
