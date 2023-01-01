from django.shortcuts import render
from django.http import HttpResponse #追加
from django.template import loader#追加
from .models import Coordinator
from .models import Coordinator2
# Create your views here.

#関数を追加
#def top(request):
#    html = loader.render_to_string('homepage/index.html')
#    return HttpResponse(html)
#    #return HttpResponse('トップページです。')

def top(request):
    #html = loader.render_to_string('homepage/index.html')#トップページの読み込み
    #return HttpResponse(html)
    context = {
        'coordinator_list':Coordinator.objects.all(),
        'coordinator_list2':Coordinator2.objects.all(),
    }
    return render(request, 'homepage/index.html', context)

def coordinator(request):
    context = {
        'coordinator_list':Coordinator.objects.all(),
        'coordinator_list2':Coordinator2.objects.all(),
    }
    return render(request, 'homepage/coordinator.html', context)


def register(request):
    return render(request, 'homepage/register.html',)

def aboutus(request):
    return render(request, 'homepage/aboutus.html',)

def contact(request):
    return render(request, 'homepage/contact.html',)

def terms_of_service(request):
    return render(request, 'homepage/terms_of_service.html',)

def privacy_policy(request):
    return render(request, 'homepage/privacy_policy.html',)

    
#test
def myroom(request):
    context = {
        'myroom_list':Myroom.objects.get(pk=1),#一つ目のデータだけを渡す。
        'stock_list':Stock.objects.all(),
    }
    return render(request, 'homepage/myroom.html', context)
