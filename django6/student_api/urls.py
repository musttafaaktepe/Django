
from django.urls import path, include
from rest_framework import routers
from .views import (
    home,
    # students_list,
    # student_create,
    # student_detail,
    # student_update,
    # student_delete,
    # student_api,
    # student_api_get_update_delete

    # StudentListCreate,
    # StudentDetail,
    # StudentGAV,
    # StudentDetailGAV,
    # StudentCV,
    # StudentDetailCV
    StudentMVS,
    PathMVS
    ) 

router = routers.DefaultRouter()
router.register("student", StudentMVS)
router.register("path", PathMVS)

urlpatterns = [
    path('', home),
    # path("student-list/", students_list, name='list'),
    # path("student-create/", student_create, name='create'),
    # path("student-detail/<int:pk>/", student_detail, name='detail'),
    # path("student-update/<int:pk>/", student_update, name='update'),
    # path("student-delete/<int:pk>/", student_delete, name='delete'),
    # path('student/', student_api),
    # path('student/<int:pk>', student_api_get_update_delete)


    # path("student/", StudentListCreate.as_view()),
    # path("student/<int:pk>", StudentDetail.as_view()),
    # path("student/", StudentGAV.as_view()),
    # path("student/<int:pk>", StudentDetailGAV.as_view()),
    # path("student/", StudentCV.as_view()),
    # path("student/<int:pk>", StudentDetailCV.as_view()),
    path("", include(router.urls))
]

#! GENERICAPIView and Mixins
