from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FeedBack, reviews
from Home.models import rating
from django.core.paginator import Paginator
from .models import feedback


def add_feedback(request):
    rating_list = rating.objects.all()
    chanels = rating.objects.all()
    if request.method == 'POST':
        form = FeedBack(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, ('Ваше сообщение отправлено'))
        return redirect('feedback')
    else:
        form = FeedBack()
        alla = Paginator(rating.objects.filter(passed = False).order_by('-id'), 8)
        stra = request.GET.get('page')
        alla = alla.get_page(stra)
    return render(request, 'feedback/feedback.html', {'form': form,
                                                      'chanels': chanels,
                                                      'rating_list': alla,
                                                      })


def add_review(request):
    chanels = rating.objects.all()
    if request.method == 'POST':
        form = reviews(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, ('Ваш запрос отправлен'))
        return redirect('review')
    else:
        form = reviews()
        alla = Paginator(rating.objects.filter(passed = False).order_by('-id'), 8)
        stra = request.GET.get('page')
        alla = alla.get_page(stra)
    return render(request, 'feedback/review.html', {'form': form,
                                                    'chanels': chanels,
                                                    'rating_list': alla})


def feedback_create(request):
    name = request.POST['name']
    email = request.POST['email']
    theme = request.POST['theme']
    message = request.POST['message']

    new_feedback = feedback(name=name, email=email, theme=theme, message=message)
    new_feedback.save()

    return JsonResponse(
        data={
            'status': 400,
            'error': 'Ваше сообщение отправлено'
        },
        status=200
    )

