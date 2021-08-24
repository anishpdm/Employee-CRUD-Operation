from django.urls import path, include
from employee import views

urlpatterns = [
   
#  Views
    path('addview/', views.add_employee_view, name='add_employee_view'),
    path('viewemployeescreen/', views.view_all_employees, name='view_all_employees'),
    path('updateemployeescreen/', views.update_view_employees, name='update_view_employees'),
    

#    API's 
    path('add/', views.employee_create, name='employee_create'),
    path('viewall/', views.employee_list, name='employee_list'),
    path('viewemployee/<fetchid>', views.employee_details, name='employee_details'),
  
]
