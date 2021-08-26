from django.urls import path, include
from employee import views

urlpatterns = [
   
#  Views
    path('addview/', views.add_employee_view, name='add_employee_view'),
    path('viewemployeescreen/', views.view_all_employees, name='view_all_employees'),
    path('updateemployeescreen/', views.update_view_employees, name='update_view_employees'),
    path('searchemployeescreen/', views.search_view_employees, name='search_view_employees'),
    path('deleteemployeescreen/', views.deleteemployeescreen, name='deleteemployeescreen'),

    

#    API's 
    path('add/', views.employee_create, name='employee_create'),
    path('viewall/', views.employee_list, name='employee_list'),
    path('viewemployee/<fetchid>', views.employee_details, name='employee_details'),
    path('searchapi/', views.searchapi, name='searchapi'),
    path('update_search_api/', views.update_search_api, name='update_search_api'),
    path('update_action_api/', views.update_data_read, name='update_data_read'),
    path('delete_search_api/', views.delete_search_api, name='delete_search_api'),
    path('delete_action_api/', views.delete_data_read, name='delete_data_read'),
  
]
