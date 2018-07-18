from django.shortcuts import render,HttpResponse

# Create your views here.
from app01 import models
def business(request):
    v1 = models.Business.objects.all()
    v2 = models.Business.objects.all().values('id','caption')
    v3 = models.Business.objects.all().values_list('id','caption')
    #QuerySet
    #[obj(id,caption,code),obj,obj]
    return render(request,'business.html',{'v1':v1,'v2':v2,'v3':v3})
def host(request):
    v1 = models.Host.objects.all()
    # for row in v1:
    #     print(row.nid,row.hostname,row.ip,row.port,row.b_id,row.b.caption,row.b.code)
    # return HttpResponse('host')
    return render(request, 'host.html', {'v1': v1})
