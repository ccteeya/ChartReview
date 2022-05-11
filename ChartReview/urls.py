"""ChartReview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from user.views import UserViewSet, MyTokenObtainPairView
from chart.views import TableViewSet, ChartViewSet, KeywordViewSet, UsersKeywordGroupViewSet, UserKeywordViewSet
from task.views import TaskViewSet, NoteViewSet
from questionnaire.views import QuestionnaireViewSet, ChoiceViewSet, AnswerViewSet

router = DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'table', TableViewSet)
router.register(r'chart', ChartViewSet)
router.register(r'task', TaskViewSet)
router.register(r'questionnaire', QuestionnaireViewSet)
router.register(r'choice', ChoiceViewSet)
router.register(r'keyword', KeywordViewSet)
router.register(r'note', NoteViewSet)
router.register(r'answer', AnswerViewSet)
router.register(r'userskeywordgroup', UsersKeywordGroupViewSet)
router.register(r'userkeyword', UserKeywordViewSet)

urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # path('api-auth/', include('rest_framework.urls')),
    # path('api/chart/', include('chart.urls', namespace='chart')),


]
admin.site.site_header = "Chart Admin"
admin.site.site_title = "Admin Portal"
admin.site.index_title = ""

from django.contrib.auth.models import User, Group
# admin.site.unregister(User)
admin.site.unregister(Group)