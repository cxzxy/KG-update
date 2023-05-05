from django.views.decorators.csrf import csrf_exempt
from app.utils.jsonResponse import json_response
from app.models import User, Settings


# 获取设置
@csrf_exempt
def get_settings(request):
    if request.method == 'GET':
        user = User.objects.filter(email=request.user_info).first()
        if user.role == 1:
            settings = Settings.objects.all()
            data_list = []
            for setting in settings:
                data = {}
                data['setting_name'] = setting.name
                data['isOpened'] = setting.isOpened
                data_list.append(data)
            data = {"settings": data_list}
            return json_response(200, '请求成功', data)
        else:
            return json_response(206, '无权限')
    else:
        return json_response(203, '请求方式错误')


# 修改设置
@csrf_exempt
def update_settings(request):
    if request.method == 'POST':
        user = User.objects.filter(email=request.user_info).first()
        if user.role == 1:
            auto_examine = request.POST.get('auto_examine')
            turn_off_permission_control = request.POST.get('turn_off_permission_control')
            if auto_examine not in ['0', '1'] or turn_off_permission_control not in ['0', '1']:
                return json_response(201, '参数类型错误')
            Settings.objects.filter(name="auto_examine").update(isOpened=auto_examine)
            Settings.objects.filter(name="turn_off_permission_control").update(isOpened=turn_off_permission_control)
            return json_response(200, '修改成功')
        else:
            return json_response(206, '无权限')
    else:
        return json_response(203, '请求方式错误')
