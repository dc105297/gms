from help.models import Alert

def alert_count_processor(request):
    alert_count = Alert.objects.filter(is_active=True).count()
    return {"alert_count":alert_count,}
