from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed


class MyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        """
        去做用户认证：读取请求传递的token、检验合法性
        三种返回值：
        1 元组(11,22)  认证成功 -> req.user req.auth
        2 抛出异常      认证失败 -> 返回错误信息
        3 返回None     多个认证类 -> 匿名用户
        """
        # 读取请求传递的token  xxx/xxx/?token=123
        token = request._request.GET['token']
        token = request._request.GET.get('token')
        token = request.query_parms.get('token')
        # 校验合法性  简化认为只要有token就认为成功
        if token:
            return ('zjs', token)  # 返回元组 认证成功
        raise AuthenticationFailed('认证失败')  # 抛出异常 认证失败


# 该API接口 不需要登录即可访问
class LoginView(APIView):
    def get(self, request, *args, **kwargs):
        return Response('返回成功LoginView')


# 该API接口 需要登录才能访问
class UserView(APIView):
    def get(self, request, *args, **kwargs):
        return Response('返回成功UserView')


# 该API接口 需要登录才能访问
class OrderView(APIView):
    def get(self, request, *args, **kwargs):
        return Response('返回成功OrderView')
