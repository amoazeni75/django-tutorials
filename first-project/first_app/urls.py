from django.urls import path
from first_app import views, advance_view

app_name = 'first_app'

urlpatterns = [
    # path('', views.index, name='index'), # this is a basic way
    path('', advance_view.IndexView.as_view(), name='cbv_index'),
    path('SchoolList', advance_view.SchoolListView.as_view(), name='list'),
    path('<int:pk>', advance_view.SchoolDetailVeiw.as_view(), name='detail'),
    path('UpdateSchool/<int:pk>', advance_view.SchoolUpdateView.as_view(), name='update'),
    path('DeleteSchool/<int:pk>', advance_view.SchoolDeleteView.as_view(), name='delete'),
    path('CreateSchool', advance_view.SchoolCreateView.as_view(), name='create'),
    path('webPages', views.show_web_pages, name='web_pages'),
    path('formName', views.form_name_view, name='form_pages'),
    path('registerWeb', views.register_web_page, name='register_web_pages'),
    path('register', views.register_user, name='register'),
    path('user_login/', views.user_login, name='user_login'),
]
