from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from twilio.rest import TwilioRestClient
from .models import ResponseTeam, Alert
from onboard.models import Student

#Twilio Credentials
ACCOUNT_SID = "ACfbb04fbbf59f26c33a55531b74ac8cae"
AUTH_TOKEN = "01a8372eb623ae796228ae3050e9c58d"

def help(request,**kwargs):
    requesting_sid = request.session.get('sid')
    requesting_student = Student.objects.get(student_id=requesting_sid)
    startAlert(requesting_student,**kwargs)
    template = loader.get_template('help/help.html')
    context = {}
    return HttpResponse(template.render(context,request))

def startAlert(requesting_student,**kwargs):
    response_team = ResponseTeam.objects.all()

    new_alert = Alert()
    new_alert.student = requesting_student
    new_alert.district = requesting_student.district
    new_alert.is_active = True
    new_alert.response_team_activated = True
    new_alert.save()
    print "New Alert Created!"
    for response_user in response_team:
        client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
        client.messages.create(
            to="+1" + response_user.phone,
            from_="+18144028190",
            body="http://darknet:8000/dashboard/alert_detail/"+ str(new_alert.alert_id)
            )
