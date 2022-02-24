from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages

from jobs.forms import FilterForm, CommentForm, JobForm
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


def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)

    comment_form = CommentForm()

    comments = job.comment_set.all()
    return render(request, 'jobs/job_detail.html', {"job": job, "comments": comments, "comment_form": comment_form})


class JobCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Job

    form_class = JobForm

    def form_valid(self, form):
        form.instance.posted_by.pk = self.request.user.pk
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_title"] = "Post Job"
        return context


class JobUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, generic.UpdateView):
    model = Job
    success_message = "Job post Updated Successfully!"
    form_class = JobForm

    def test_func(self):
        job = self.get_object()
        return True if self.request.user.pk == job.posted_by.pk else False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_title"] = "Update Job"
        return context


class JobDeleteView(LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin, generic.DeleteView):
    model = Job
    # success_message = 'Post Deleted Successfully!'
    success_url = 'job_list'

    def test_func(self):
        job = self.get_object()
        return True if self.request.user.pk == job.posted_by.pk else False

    def delete(self, request, *args, **kwargs):
        # messages.success(self.request, self.success_message)
        return super(JobDeleteView, self).delete(request, *args, **kwargs)


@login_required
def add_comment(request, pk):
    message = request.POST.get("message")
    job = Job.objects.get(pk=pk)
    Comment.objects.create(message=message, user=request.user, job=job)

    return redirect("job_detail", pk=pk)


@login_required
def delete_comment(request, pk, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    comment.delete()
    return redirect("job_detail", pk)
