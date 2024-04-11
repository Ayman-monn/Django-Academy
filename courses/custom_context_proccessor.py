from .models import Notification


def notifications(request):
    notifications = Notification.objects.select_related('lesson', 'comment', 'from_user').filter(to_user=request.user.username) 
    un_seen = notifications.filter(is_seen=False).count()    
    return {
        'notifications':notifications,
        'un_seen':un_seen
    }

