from django.shortcuts import render
from django.template import Context
# Create your views here.
from django.shortcuts import HttpResponse,render,redirect
from django.shortcuts import render_to_response
from cmdb import models
USER_DICT  ={
   'k1' :{'root1'},
   'k2': {'root1'},
   'k3': {'root1'},
   'k4': {'root1'},
}
def index(request):
   return render(request,'index.html',{'user_dict':USER_DICT})

def login(request):
   error_msg = ""
   if request.method == "POST" :
      user = request.POST.get('user',None)
      pwd = request.POST.get('pwd',None)
      if user == 'root' and pwd == '123':
         return render(request,'home.html')
      else:
         error_msg = "用户名密码错误！"

   return render(request,'login.html',{'error_msg':error_msg})

USER_LIST = [
    {'id': 1, 'username': 'alex', 'email': 'asdfasdf', "gender": '男'},
    {'id': 2, 'username': 'eriuc', 'email': 'asdfasdf', "gender": '男'},
    {"id": 3,'username': 'seven', 'email': 'asdfasdf', "gender": '男'},
]


def list(request):
   people_list = models.message.objects.all()
  # c = Context({"people_list": people_list})
   return render(request,"showuser.html", {"people_list": people_list})

def itzc(request):
    if request.method == "POST":
        jqm = request.POST.get("jqm", None)
        ipaddr = request.POST.get("ipaddr", None)
        user = request.POST.get("user", None)
        userpwd = request.POST.get("userpwd", None)
        addr = request.POST.get("addr", None)
        paydate = request.POST.get("paydate", None)
        obj = models.itzc.objects.create(jqm=jqm, ipaddr=ipaddr,user=user,userpwd=userpwd, addr=addr ,paydate=paydate )
        obj.save()
    return render(request,'itzc.html')


def insert(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        obj = models.message.objects.create(username=username, password=password)
        obj.save()
    return render(request,'insert.html')

def home(request):
   if request.method == 'POST':
      u = request.POST.get('username')
      e = request.POST.get('email')
      g = request.POST.get('gender')
      temp = {'username': u, 'email': e, "gender": g}
      USER_LIST.append(temp)
   return render(request,'home.html',{'user_list':  USER_LIST})