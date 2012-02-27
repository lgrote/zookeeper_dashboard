from django.shortcuts import render_to_response
from django.conf import settings

from zookeeper_dashboard.zkadmin.models import ZKServer
from zookeeper_dashboard.zktree.models import ZNode

ZOOKEEPER_SERVERS = getattr(settings,'ZOOKEEPER_SERVERS').split(',')

def index(request):
    server_data = []
    for i, server in enumerate(ZOOKEEPER_SERVERS):
        zkserver = ZKServer(server)
        zkserver.id = i
        server_data.append(zkserver)
        
    rootNode = ZNode()
    children = rootNode.getExtendedChildren()
    quotaNode = ZNode("/zookeeper/quota")

    return render_to_response('zkadmin/index.html',
                              {'ZOOKEEPER_SERVERS':ZOOKEEPER_SERVERS,
                               'server_data':server_data,
                               'rootNode':rootNode,
                               'children':children,
                               'quotaNode':quotaNode})

def detail(request, server_id):
    server_data = ZKServer(ZOOKEEPER_SERVERS[int(server_id)])
    server_data.id = server_id
    return render_to_response('zkadmin/detail.html',
                              {'server_data':server_data})
