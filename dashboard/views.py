from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from help.models import Alert
from onboard.models import Student

#The "user" var unless explicitly stated refers to the management user such as teacher,pricipal,etc.


def dashboardLogin(request,**kwargs):
    template = loader.get_template('dashboard/dashboard_login.html')
    context = {}
    return HttpResponse(template.render(context,request))

def dashboardAuth(request,**kwargs):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/dashboard/')
    else:
        response = HttpResponse("Fail")
        return response

@login_required
def dashboard(request,**kwargs):
    template = loader.get_template('dashboard/dashboard.html')
    #Get an active alert count
    alert_count = Alert.objects.filter(is_active=True).count()
    context = {"alert_count":alert_count,}
    return HttpResponse(template.render(context,request))

@login_required
def manageAlerts(request,**kwargs):
    template = loader.get_template('dashboard/alerts.html')
    alert_list = Alert.objects.all().order_by('-alert_created')
    context = {'alert_list':alert_list,}
    return HttpResponse(template.render(context,request))

@login_required
def alertDetail(request,uuid,**kwargs):
    template = loader.get_template('dashboard/alert_detail.html')
    alert_list = Alert.objects.all()
    context = {'alert_list':alert_list,}
    return HttpResponse(template.render(context,request))

@login_required
def manageStudents(request,**kwargs):
    template = loader.get_template('dashboard/manage_students.html')
    user = request.user
    student_list = Student.objects.filter(district=user.profile.district.id)
    context = {'student_list':student_list,}
    return HttpResponse(template.render(context,request))

@login_required
def studentProfile(request,student_id,**kwargs):
    template = loader.get_template('dashboard/manage_students.html')
    student = Student.objects.get(student_id=student_id)
    context = {}
    return HttpResponse(template.render(context,request))
