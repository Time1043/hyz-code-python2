"""django231103 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app01 import views
from app01.views import depart, user, pretty,admin

urlpatterns = [
    # 管理员
    path("admin/list/", admin.admin_list),
    path("admin/add/", admin.admin_add),
    path("admin/dlt/", admin.admin_dlt),
    path("admin/<int:nid>/edit/", admin.admin_edit),

    # 部门管理
    path("depart/list/", depart.depart_list),
    path("depart/add/", depart.depart_add),
    path("depart/dlt/", depart.depart_dlt),
    path("depart/<int:nid>/edit/", depart.depart_edit),

    # 用户管理
    path("user/list/", user.user_list),
    path("user/add/", user.user_add),
    path("user/dlt/", user.user_dlt),
    path("user/<int:nid>/edit/", user.user_edit),

    path("user/model/form/add/", user.user_model_form_add),
    path("user/model/form/<int:nid>/edit/", user.user_model_form_edit),

    # 靓号管理
    path("pretty/list/", pretty.pretty_list),
    path("pretty/model/form/add/", pretty.pretty_model_form_add),
    path("pretty/dlt/", pretty.pretty_dlt),
    path("pretty/model/form/<int:nid>/edit/", pretty.pretty_model_form_edit),
]
