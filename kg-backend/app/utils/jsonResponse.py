from django.http import JsonResponse


def json_response(code=200, msg='请求成功', data=None):
    json_dict = {
        'code': code,
        'msg': msg,
    }
    if data is not None:
        json_dict.update({'data': data})
    return JsonResponse(json_dict, json_dumps_params={"ensure_ascii": False})
