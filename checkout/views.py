from django.shortcuts import  render
from django.http import  JsonResponse
from django.core.mail import send_mail
from courses.models import Course, StudentCourses
from academy_project import settings 
import stripe
from courses.models import Course
import math


def create_payment(request, pk):
    course = Course.objects.get(pk=pk)
    # student = StudentCourses.objects.select_related('user', 'course').get(course =course) 
    # if student: 
    #     return redirect('MyCourses')
    try:
        stripe.api_key = settings.STRIPE_SECRET_KEY
        intent = stripe.PaymentIntent.create(
            amount=math.ceil(course.price * 100),
            currency=settings.CURRENCY,
            payment_method_types=['card'],
            metadata={
                'course_id': course.id,
                'user_id': request.user.id
            }
        )
        return JsonResponse({
            'clientSecret': intent['client_secret']
        })
    except Exception as e:
        return JsonResponse({ 'error': str(e) })
    


def checkout_complete(request):
    return render(request, 'checkout-complete.html')