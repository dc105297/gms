from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from onboard.models import Student
from onboard.models import Student

def index(request,**kwargs):
    student_id = None
    if 'sid' in request.session:
        student_id = request.session['sid']
    if student_id is None:
        return HttpResponseRedirect('/onboard/')
    else:
        template = loader.get_template('index/index.html')
        context = {"student_id":student_id}
        return HttpResponse(template.render(context,request))


#This takes in POST data from the onboard page form. Then sets a session realting to the student ID.
#Checks if the student is already active.
#If student is not active then the session is created and the student becomes activated.
#Currently in order to allow a student to log back in if a session expires is to manually deactive the student from dashboard.
def setStudent(request,**kwargs):
    student_id = None
    if request.method == "POST":
        sd = request.POST
        student_id = sd["student_id"]

    student = Student.objects.get(student_id=student_id)
    if student.activated is True:
        response = HttpResponse("That Student ID is already Registered!")
        return response
    else:
        request.session['sid'] = student_id
        student.activated = True
        student.save()
        return HttpResponseRedirect('/')
