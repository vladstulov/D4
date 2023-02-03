from django.urls import path
from .views import NewsList, NewsDetail, NewsSearchList, NewsAddList, NewsEditView, NewsDeleteView

urlpatterns = [
    path('', NewsList.as_view()),
    path('search', NewsSearchList.as_view()),
    path('add', NewsAddList.as_view()),
    path('<int:pk>', NewsDetail.as_view(), name = 'note'),
    path('<int:pk>/edit', NewsEditView.as_view(), name = 'newsEdit'),
    path('<int:pk>/delete', NewsDeleteView.as_view(), name = 'newsDelete'),
]
