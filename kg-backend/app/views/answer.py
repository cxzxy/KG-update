from django.views.decorators.csrf import csrf_exempt
from app.utils.jsonResponse import json_response
from app.models import Document, User, QApair, DocumentField


@csrf_exempt
def get_answer(request):
    if request.method == 'POST':
        user = User.objects.filter(email=request.user_info).first()
        username = user.username
        user_id = user.user_id
        document_id = request.POST.get('document_id')
        question = request.POST.get('question')
        document = Document.objects.filter(document_id=document_id).first()
        field = DocumentField.objects.filter(id=document.field.id).first().field_name
        title = document.title
        summary = document.content[:20]
        # 临时答案
        answer = "您的提问是“" + question + "”，这是针对于" + field + "领域的文章《" + title + "》 :" + summary + "...的回答"
        # 存储问答对
        QApair.objects.create(user_id=user_id, document_id=document, question=question, answer=answer)
        return json_response(200, '请求成功', {'answer': answer})
    else:
        return json_response(203, '请求方式错误')


# 获取问答对列表
@csrf_exempt
def get_answer_list(request):
    if request.method == 'GET':
        user = User.objects.filter(email=request.user_info).first()
        user_id = user.user_id
        answer_list = QApair.objects.filter(user_id=user_id).values()
        print(answer_list)
        answers = []
        for answer in answer_list:
            answer_dict = {}
            answer_dict['id'] = answer['id']
            answer_dict['question'] = answer['question']
            answer_dict['answer'] = answer['answer']
            answer_dict['document_id'] = answer['document_id_id']
            answers.append(answer_dict)
        data = {'data': answers}
        return json_response(200, '请求成功', data)
    else:
        return json_response(203, '请求方式错误')


# 删除问答对
@csrf_exempt
def delete_answer(request):
    if request.method == 'POST':
        user = User.objects.filter(email=request.user_info).first()
        id = request.POST.get('id')
        if QApair.objects.filter(id=id, user_id=user.user_id).first() is None:
            return json_response(204, '该问答对不存在')
        else:
            QApair.objects.filter(id=id, user_id=user.user_id).first().delete()
        return json_response(200, '删除成功')
    else:
        return json_response(203, '请求方式错误')
