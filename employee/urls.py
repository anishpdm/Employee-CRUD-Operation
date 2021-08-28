from django.urls import path, include
from employee import views

urlpatterns = [
   
#  Views
    path('addview/', views.add_employee_view, name='add_employee_view'),
    path('viewemployeescreen/', views.view_all_employees, name='view_all_employees'),
    path('updateemployeescreen/', views.update_view_employees, name='update_view_employees'),
    path('searchview/', views.search_view_employees, name='search_view_employees'),
    path('deleteview/', views.delete_view_employees, name='delete_view_employees'),
    path('loginview/', views.loginview, name='loginview'),


#    API's 
    path('add/', views.employee_create, name='employee_create'),
    path('search/', views.searchapi, name='searchapi'),
    path('Update_Search_api/', views.Update_Search_api, name='Update_Search_api'),
    path('Delete_Search_api/', views.Delete_Search_api, name='Delete_Search_api'),
    path('login_check/', views.login_check, name='login_check'),

    path('viewall/', views.employee_list, name='employee_list'),
    path('viewemployee/<fetchid>', views.employee_details, name='employee_details'),
    path('viewemployee/deletebtn/', views.employee_details_deletebtn, name='employee_details_deletebtn'),
    path('viewemployee/updatebtn/', views.employee_details_updatebtn, name='employee_details_updatebtn'),
  
]
