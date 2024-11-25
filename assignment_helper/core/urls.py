from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    

    path('create_quiz/',views.create_quiz,name='create_quiz'),
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.sign_up, name='sign_up'),
    path('log_out/', views.log_out, name='log_out'),
    path('upload/', views.upload_pdf, name='upload_pdf'),
    path('saved_files/', views.saved_files, name='saved_files'),
    path('edit_file_details/', views.edit_file_details, name='edit_file_details'),
    path('update_questions/', views.update_questions, name='update_questions'),
    path('api/uploaded-files/', views.get_uploaded_files, name='get_uploaded_files'),
    path('delete_file/<int:file_id>/', views.delete_file, name='delete_file'),
    path('generate_answer/', views.generate_answer, name='generate_answer'),
    path('generate_answers/', views.generate_answers, name='generate_answers'),
    path('view_answers/<int:file_id>/', views.view_answers, name='view_answers'),  # New URL pattern for viewing answers
    path('download/<int:file_id>/', views.download_file, name='download_file'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)