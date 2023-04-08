from django.views.decorators.csrf import csrf_exempt
from app.utils.jsonResponse import json_response
from app.models import Graph, User


# 获取图谱列表
@csrf_exempt
def get_graph_list(request):
    if request.method == 'GET':
        username = User.objects.filter(email=request.user_info).first().username
        graph = Graph.objects.filter(username=username).first()
        if graph:
            graph = graph.graph
            Nodes = []
            Edges = []
            for node in graph['Vertices']:
                Node = {}
                Node['id'] = node['id']
                Node['name'] = node['properties']['name']
                Node['entity_type'] = node['entity_type']['name']
                Nodes.append(Node)
            for edge in graph['Edges']:
                Edge = {}
                Edge['source'] = edge['start_id']
                Edge['target'] = edge['target_id']
                Edge['value'] = edge['relationship_type']['name']
                Edges.append(Edge)
            data = {}
            data['Nodes'] = Nodes
            data['Edges'] = Edges
            return json_response(200, '请求成功', data)
        else:
            return json_response(206, '请求成功', {'Nodes': [], 'Edges': []})
    else:
        return json_response(203, '请求方式错误')
