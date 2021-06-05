from django.urls import path, include
from finances.views import *


urlpatterns = [
    path('', blanc),

    path('user/create/', UserCreateView.as_view()),
    path('user/info/<int:pk>/', UserRUDView.as_view()),
    path('transaction/create/', TransactionCreateView.as_view()),
    path('transaction/info/<int:pk>/', TransactionRUDView.as_view()),
    path('user/detail/<int:pk>/', UserDetailView.as_view()),
    path('user/detail/daily/<int:pk>/', UserTotalView.as_view()),

    # Do not pay attention, it's just for you to see what errors it produces
    path('user/detail/daily2/<int:pk>/', UserDailyTotalView.as_view())

]