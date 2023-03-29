from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from main import views

urlpatterns = [
    path('dream/v1/id/<id>', views.ListDreambyID.as_view()),
    path('dream/v1/allquotes',views.GetAllQuotes.as_view())
]

urlpatterns= format_suffix_patterns(urlpatterns)