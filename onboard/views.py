from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

def onboard(request,**kwargs):
    template = loader.get_template('onboard/onboard.html')
    context = {}
    return HttpResponse(template.render(context,request))
