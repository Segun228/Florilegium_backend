from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

class TelegramAuthView(APIView):
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
            "user_id": user.telegram_id,
            "username": user.username,
            "created": created
        }, status=status.HTTP_200_OK)
