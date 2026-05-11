from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.utils.translation import gettext_lazy as _

from .models import ReportedIssue
from .forms import ReportIssueForm


class ReportIssueView(LoginRequiredMixin, CreateView):
    """View for residents to report issues."""
    model = ReportedIssue
    form_class = ReportIssueForm
    template_name = 'report_issue/report_issue.html'
    success_url = reverse_lazy('report_issue_success')

    def form_valid(self, form):
        form.instance.reported_by = self.request.user
        messages.success(self.request, 'Problema a fost raportată cu succes!')
        return super().form_valid(form)


class ReportIssuePublicView(CreateView):
    """Public view for anyone to report issues."""
    model = ReportedIssue
    form_class = ReportIssueForm
    template_name = 'report_issue/report_issue_public.html'
    success_url = reverse_lazy('report_issue_success')

    def form_valid(self, form):
        messages.success(self.request, 'Problema a fost raportată cu succes! Vă vom contacta în curând.')
        return super().form_valid(form)


class IssueListView(PermissionRequiredMixin, ListView):
    """View for admins to list all reported issues."""
    model = ReportedIssue
    template_name = 'report_issue/issue_list.html'
    context_object_name = 'issues'
    permission_required = 'report_issue.view_reportedissue'
    paginate_by = 20


class IssueUpdateView(PermissionRequiredMixin, UpdateView):
    """View for admins to update issue status."""
    model = ReportedIssue
    form_class = ReportIssueForm
    template_name = 'report_issue/issue_update.html'
    success_url = reverse_lazy('issue_list')
    permission_required = 'report_issue.change_reportedissue'

    def form_valid(self, form):
        messages.success(self.request, 'Statusul problemei a fost actualizat!')
        return super().form_valid(form)


def report_issue_success(request):
    """Success page after reporting an issue."""
    return render(request, 'report_issue/report_issue_success.html')
