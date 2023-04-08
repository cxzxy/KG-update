from django.views.decorators.csrf import csrf_exempt
from app.utils.jsonResponse import json_response
from app.models import Document, User, DocumentField, Settings
import time
from datetime import datetime
from django.http import QueryDict


# 上传文献，有权限控制
@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        field = request.POST.get('field')
        Field = DocumentField.objects.filter(field_name=field).first()
        if Field is None:
            return json_response(205, '该领域不存在')
        status=Settings.objects.filter(name="auto_examine").first().isOpened
        content = request.POST.get('content')
        create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 获取当前时间戳
        update_time = create_time
        user = User.objects.filter(email=request.user_info).first()
        user_role = user.role
        userid = user.user_id
        user_id = User.objects.get(user_id=userid)
        file = Document(field=Field, create_time=create_time, update_time=update_time, status=status, title=title,
                        content=content, user=user_id)
        file.save()
        return json_response(200, '上传成功')
    else:
        return json_response(203, '请求方式错误')


# 搜索文献，有权限控制
@csrf_exempt
def search_file_list(requset):
    if requset.method == 'GET':
        title = requset.GET.get('title')
        file_list = Document.objects.filter(title__contains=title).values()
        files = []
        for file in file_list:
            file_dict = {}  # 必须放在循环内部
            file_dict['document_id'] = file['document_id']
            file_dict['title'] = file['title']
            file_dict['field'] = DocumentField.objects.filter(id=file['field']).first().field
            files.append(file_dict)
        data = {'data': files}
        return json_response(200, '请求成功', data)
    else:
        return json_response(203, '请求方式错误')


# 获取某个文献详细内容，无权限控制
@csrf_exempt
def get_file_detail(request):
    if request.method == 'GET':
        document_id = request.GET.get('document_id')
        document = Document.objects.filter(document_id=document_id).first()
        file_dict = {}
        file_dict['document_id'] = document.document_id
        file_dict['field'] = DocumentField.objects.filter(id=document.field).first().field
        file_dict['title'] = document.title
        file_dict['create_time'] = document.create_time
        file_dict['update_time'] = document.update_time
        file_dict['status'] = document.status
        file_dict['content'] = document.content
        file_dict['author'] = document.user.username
        return json_response(200, '请求成功', file_dict)
    else:
        return json_response(203, '请求方式错误')


# 获取已通过审核的文献列表，无权限控制
@csrf_exempt
def get_success_files(request):
    if request.method == 'GET':
        user_id = User.objects.filter(email=request.user_info).first().user_id
        files = Document.objects.select_related('auditor').all().filter(user=user_id, status=1)
        file_list = []
        for file in files:
            file_dict = {}
            file_dict['document_id'] = file.document_id
            file_dict['field'] = file.field.field_name
            file_dict['title'] = file.title
            file_dict['create_time'] = file.create_time
            # file_dict['update_time'] = file.update_time
            file_list.append(file_dict)
        return json_response(200, '请求成功', file_list)
    else:
        return json_response(203, '请求方式错误')


# 获取未通过审核的文献列表，无权限控制
# @csrf_exempt
# def get_failure_files(request):
#     if request.method == 'GET':
#         user_id = User.objects.filter(email=request.user_info).first().user_id
#         files = Document.objects.select_related('auditor').all().filter(user=user_id, status=2)
#         file_list = []
#         for file in files:
#             file_dict = {}
#             file_dict['document_id'] = file.document_id
#             file_dict['field'] = file.field
#             file_dict['title'] = file.title
#             file_dict['create_time'] = file.create_time
#             file_dict['update_time'] = file.update_time
#             file_dict['status'] = file.status
#             file_dict['content'] = file.content
#             file_dict['reason'] = file.reason
#             file_dict['author'] = file.auditor.username
#             file_list.append(file_dict)
#         return json_response(200, '请求成功', file_list)
#     else:
#         return json_response(203, '请求方式错误')


# 获取上传过的文献列表，无权限控制
# @csrf_exempt
# def get_uploaded_files(request):
#     if request.method == 'GET':
#         user_id = User.objects.filter(email=request.user_info).first().user_id
#         files = Document.objects.filter(user=user_id).values()
#         return json_response(200, '请求成功', list(files))
#     else:
#         return json_response(203, '请求方式错误')


# 获取未审核的文献列表，管理员专属
@csrf_exempt
def get_unaudited_files(request):
    if request.method == 'GET':
        user = User.objects.filter(email=request.user_info).first()
        if user.role == 1:
            files = Document.objects.filter(status=0).values()
            return json_response(200, '请求成功', list(files))
        else:
            return json_response(206, '无权限该操作')
    else:
        return json_response(203, '请求方式错误')


# 审核文献，管理员专属
@csrf_exempt
def examine_file(request):
    if request.method == 'PUT':
        user = User.objects.filter(email=request.user_info).first()
        if user.role == 1:
            data = QueryDict(request.body)
            file = Document.objects.filter(document_id=data.get('document_id'), status=0).first()
            if file is None:
                return json_response(200, '请求成功', file)
            file.status = data.get('status')
            file.reason = data.get('reason')
            file.auditor = user
            file.save()
            file = Document.objects.filter(document_id=data.get('document_id')).values().first()
            return json_response(200, '请求成功', file)
        else:
            return json_response(206, '无权限该操作')
    else:
        return json_response(203, '请求方式错误')


# 获取已审核成功的文献列表 管理员专属
# @csrf_exempt
# def get_file_list(request):
#     if request.method == 'GET':
#         user = User.objects.filter(email=request.user_info).first()
#         if user.role == 1:
#             files = Document.objects.select_related('auditor').all().filter(status=1)
#             file_list = []
#             for file in files:
#                 file_dict = {}
#                 file_dict['document_id'] = file.document_id
#                 file_dict['field'] = file.field
#                 file_dict['title'] = file.title
#                 file_dict['create_time'] = file.create_time
#                 file_dict['update_time'] = file.update_time
#                 file_dict['status'] = file.status
#                 file_dict['content'] = file.content
#                 file_dict['author'] = file.auditor.username
#                 file_list.append(file_dict)
#             return json_response(200, '请求成功', file_list)
#         else:
#             return json_response(206, '无权限该操作')
#     else:
#         return json_response(203, '请求方式错误')


# 修改文献，管理员专属
@csrf_exempt
def change_file(request):
    if request.method == 'POST':
        user = User.objects.filter(email=request.user_info).first()
        if user.role == 1:
            data = request.POST
            print(data.get('status'))
            if int(data.get('status')) != 1:
                return json_response(207, '该文献未审核成功')
            file = Document.objects.filter(document_id=data.get('document_id')).first()
            file.title = data.get('title')
            if DocumentField.objects.filter(field_name=data.get('field')).first() is None:
                return json_response(208, '该领域不存在')
            file.field = data.get('field')
            file.update_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            file.content = data.get('content')
            file.save()
            return json_response(200, '修改成功')
        else:
            return json_response(206, '无权限该操作')
    else:
        return json_response(203, '请求方式错误')


# 删除文献，管理员专属
@csrf_exempt
def delete_file(request):
    if request.method == 'DELETE':
        user = User.objects.filter(email=request.user_info).first()
        if user.role == 1:
            data = QueryDict(request.body)
            if Document.objects.filter(document_id=data.get('document_id')).exists():
                Document.objects.filter(document_id=data.get('document_id')).delete()
                return json_response(200, '删除成功')
            else:
                return json_response(320, '该文献不存在')
        else:
            return json_response(206, '无权限该操作')
    else:
        return json_response(203, '请求方式错误')
