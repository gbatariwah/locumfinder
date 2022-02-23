from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views import generic

from jobs.forms import FilterForm, CommentForm
from jobs.models import Job, Comment


def job_list(request):
    jobs = Job.objects.order_by("-created_at")

    job_type = request.GET.get("type")
    order = request.GET.get("order")
    region = request.GET.get("region")

    if job_type:
        jobs = Job.objects.filter(type=job_type)

        if region != "all":
            jobs = jobs.filter(region=region)

        if order == 'newest to oldest':
            jobs = jobs.order_by("-created_at")
        elif order == "region: a to z":
            jobs = jobs.order_by("region")
        else:
            jobs = jobs.order_by("-region")

        filter_form = FilterForm(request.GET)
        filters = {'type': job_type, 'order': order, 'region': region}

    else:
        filter_form = FilterForm()
        filters = None

    paginator = Paginator(jobs, 6)
    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj, "filter_form": filter_form, "filters": filters}

    return render(request, 'jobs/job_list.html', context)


def job_detail(request, uid):
    job = get_object_or_404(Job, uid=uid)

    comment_form = CommentForm()

    if request.method == 'POST':
        message = request.POST.get("message")
        comment = Comment(message=message, user=request.user, job=job)
        comment.save()

    comments = Comment.objects.filter(job=job)
    return render(request, 'jobs/job_detail.html', {"job": job, "comments": comments, "comment_form": comment_form})