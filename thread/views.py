from django.shortcuts import render, redirect
from django.urls import reverse
from users.models import AbstractUser
from .models import Thread, ThreadComment

def homepage(request):
    thread = Thread.objects.all()
    feedback = ThreadComment.objects.all().order_by('-id')
    th = Thread()
    if request.method == "POST":
        th.author = AbstractUser.objects.get(user=request.user)
        th.content = request.POST.get('content')
        if request.FILES.get('foto'):
            th.gambar = request.FILES.get('foto')
        th.save()
        redirect('home')
    if request.method == "GET":
        params = request.GET.get('search', '')
        thread = thread.filter(content__icontains=params)
        feedback = feedback.filter(comment__icontains=params)

    return render(request, 'homepage/home.html', {'thread': thread, 'feedback': feedback})

def detail_thread(request, thread_id):
    thread = Thread.objects.get(id=thread_id)
    thcomments = ThreadComment.objects.all().filter(ref_thread=thread).order_by('-id')
    comment = ThreadComment()
    if request.method == "POST":
        comment.ref_thread = thread
        comment.user = AbstractUser.objects.get(user=request.user)
        comment.comment = request.POST.get('comment')
        comment.save()
        order_detail_url = reverse('detail_thread', kwargs={'thread_id': thread_id})
        return redirect(order_detail_url)
    return render(request, 'thread/detail_thread.html', {'thread': thread, 'comments': thcomments})