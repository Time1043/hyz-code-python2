# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/11/8 20:05
# @File    ：admin.py
# @Function:

from django.shortcuts import render, redirect

from app01.models import Admin
from app01.utils.form import AdminModelForm
from app01.utils.pagination import Pagination


def admin_list(request):
    """ 管理员列表 """
    # 条件筛选
    data_dict = {}
    search_data = request.GET.get('q', '')  # 有值拿值 没值空字符串
    if search_data:  # 考虑空字典情况
        data_dict['mobile__contains'] = search_data

    queryset = Admin.objects.filter(**data_dict)
    page_object = Pagination(request, queryset, page_size=18)
    context = {
        'search_data': search_data, # 条件筛选
        'list_admin': page_object.page_queryset,  # 分完页的数据
        'page_string': page_object.html()  # 页码
    }
    return render(request, 'admin_list.html', context)


def admin_add(request):
    """ 管理员添加 """
    if request.method == 'GET':
        form = AdminModelForm()
        return render(request, 'admin_add.html', {'form': form})
    # POST
    form = AdminModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')
    # 检验失败
    return render(request, 'admin_add.html', {'form': form})


def admin_dlt(request):
    """ 管理员删除 """
    admin_id = request.GET.get('nid')
    Admin.objects.filter(id=admin_id).delete()
    return redirect('/admin/list/')


def admin_edit(request, nid):
    """ 管理员编辑 """
    row = Admin.objects.filter(id=nid).first()
    if request.method == 'GET':
        form = AdminModelForm(instance=row)
        return render(request, 'admin_edit.html', {'form': form})
    # POST
    form = AdminModelForm(data=request.POST, instance=row)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')
    # 不合法数据
    return render(request, 'admin_edit.html', {'form': form})
