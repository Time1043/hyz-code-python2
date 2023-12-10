from django.http import JsonResponse
from django.views import View  # django视图函数UserView需继承View
from rest_framework.views import APIView  # drf视图函数InfoView需要继承APIView
from rest_framework.response import Response


class UserView(View):
    # request原始的 包含请求相关所有数据
    def get(self, request, *args, **kwargs):
        return JsonResponse({'status': True, 'message': 'GET'})

    def post(self, request, *args, **kwargs):
        return JsonResponse({'status': True, 'message': 'POST'})

    def put(self, request, *args, **kwargs):
        return JsonResponse({'status': True, 'message': 'PUT'})

    def delete(self, request, *args, **kwargs):
        return JsonResponse({'status': True, 'message': 'DELETE'})


class InfoView(APIView):
    # request经过drf处理的 —— request=self.initialize_request(request, *args, **kwargs)
    def get(self, request, *args, **kwargs):
        return Response({'status': True})

    def post(self, request, *args, **kwargs):
        return Response({'status': True})

    def put(self, request, *args, **kwargs):
        return Response({'status': True})

    def delete(self, request, *args, **kwargs):
        return Response({'status': True})
