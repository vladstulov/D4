from django_filters import FilterSet
from .models import News

class NewsFilter(FilterSet):
   class Meta:
        model = News
        fields = {
            'title': ['icontains'],
            'dateCreation': ['lt'],
            'author': ['icontains'],
        }