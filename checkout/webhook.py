import stripe
from academy_project import settings 
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User 
from courses.models import Course, StudentCourses
from django.core.mail import send_mail
from django.template.loader import render_to_string


stripe.api_key = settings.STRIPE_ENDPOINT_SECRET



@csrf_exempt
def strip_webhook(request):
    event = None
    payload = request.body 
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_ENDPOINT_SECRET
        )
    except ValueError as e:
        print('Invalid payload')
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        print('Invalid signature')
        return HttpResponse(status=400) 

    # Handle the event
    if event.type == 'payment_intent.succeeded':
        payment_intent = event.data.object
        print('payment_intent.successede')
        course_id = payment_intent.metadata.course_id
        user_id = payment_intent.metadata.user_id
        course_access(user_id, course_id) 
        print(payment_intent.metadata)
    # ... handle other event types
    else:
        print('Unhandled event type {}'.format(event['type']))

    return HttpResponse(status=200) 


def course_access(user_id, course_id): 
    course = Course.objects.get(pk=course_id) 
    user = User.objects.get(pk=user_id) 
    StudentCourses.objects.create(course=course, user=user, amount_paid=course.price) 

    msg_html= render_to_string('emails/course.html',{
            'course': course, 
            'user': user
        })
    send_mail(
            subject='New order', 
            html_message= msg_html, 
            message=msg_html, 
            from_email='noreplay@example.com',
            recipient_list=[user.email], 
        )
        