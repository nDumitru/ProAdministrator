from django.urls import path
from . import views

app_name = 'report_issue'

urlpatterns = [
    path('raporteaza-problema/', views.ReportIssueView.as_view(), name='report_issue'),
    path('raporteaza/', views.ReportIssuePublicView.as_view(), name='report_issue_public'),
    path('problema-raportata/', views.report_issue_success, name='report_issue_success'),
    path('probleme/', views.IssueListView.as_view(), name='issue_list'),
    path('problema/<int:pk>/actualizeaza/', views.IssueUpdateView.as_view(), name='issue_update'),
]
