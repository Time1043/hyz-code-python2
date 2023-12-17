from rest_framework.response import Response
from rest_framework.views import APIView


class UserView(APIView):
    def get(self, request):
        print(request.user)  # 当前登录的用户 - drf默认的匿名用户
        print(request.auth)  # 认证
        return Response('drf的CBV返回成功')
