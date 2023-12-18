from rest_framework.response import Response
from rest_framework.views import APIView
from ext.auth import URLAuthentication, HeaderAuthentication, BodyAuthentication, NoAuthentication


# 该API接口 不需要登录即可访问
class LoginView(APIView):
    authentication_classes = []

    def get(self, request, *args, **kwargs):
        print(request.user, request.auth)  # None None
        return Response('返回成功LoginView')


# 该API接口 需要登录才能访问
class UserView(APIView):
    def get(self, request, *args, **kwargs):
        self.dispatch()
        print(request.user, request.auth)
        return Response('返回成功UserView')


# 该API接口 需要登录才能访问
class OrderView(APIView):
    authentication_classes = [URLAuthentication, HeaderAuthentication, BodyAuthentication, NoAuthentication]

    def get(self, request, *args, **kwargs):
        print(request.user, request.auth)
        return Response('返回成功OrderView')
