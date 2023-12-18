from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed


class MyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request._request.GET.get('token')
        if token:
            return ('zjs', token)  # 返回元组 认证成功
        raise AuthenticationFailed({'code': 20000, 'error': '认证失败'})  # 抛出异常 认证失败

    def authenticate_header(self, request):
        return 'token API'

class URLAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # token = request._request.GET.get('token')
        token = request.query_params.get('token')
        if token:
            return ('zjs', token)
        return  # 认证失败不报错 直接return 继续执行下一个认证组件、


class HeaderAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')
        if token:
            return ('zjs', token)
        return  # 认证失败不报错 直接return 继续执行下一个认证组件


class BodyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.data.get('token')
        if token:
            return ('zjs', token)
        return  # 认证失败不报错 直接return 继续执行下一个认证组件


class NoAuthentication(BaseAuthentication):
    def authenticate(self, request):
        raise AuthenticationFailed({'code': 20000, 'msg': '认证失败'})

