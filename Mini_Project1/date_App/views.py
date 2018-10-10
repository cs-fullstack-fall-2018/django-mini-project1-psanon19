from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import PostForm
from .models import TimeSheet

def index(request):
    posts = TimeSheet.objects.filter(date_of_entry__lte=timezone.now()).order_by('date_of_entry')
    return render(request, 'date_App/post_list.html', {'posts': posts})


def timesheet_detail(request, pk):
    post = get_object_or_404(TimeSheet, pk=pk)
    return render(request, 'date_App/post_detail.html', {'TimeSheet': post})