from django.urls import *
from .views import *

urlpatterns = [
    path('', show_blog, name="show_blog"),
    path('<int:post_id>/', post_detail, name="post_detail")

]
