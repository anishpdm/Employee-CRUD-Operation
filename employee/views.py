from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from employee.serializers import EmployeeSerializer
from employee.models import Employee
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests


def update_view_employees(request):
    return render(request, 'update.html')
    
def view_all_employees(request):

    fetchdata=requests.get("http://localhost:8000/employee/viewall/").json()

    return render(request,'viewall.html',{"data":fetchdata})

def add_employee_view(request):
    return render(request,'index.html')


@csrf_exempt
def employee_details(request, fetchid):
    try:
        employees = Employee.objects.get(id=fetchid)
        if (request.method == "GET"):
            employee_serializer = EmployeeSerializer(employees)
            return JsonResponse(employee_serializer.data, safe=False, status=status.HTTP_200_OK)
       
        if (request.method == "DELETE"):
            employees.delete()
            return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)

        if (request.method == "PUT"):
            mydata=JSONParser().parse(request)
            employee_serialize = EmployeeSerializer(employees,data=mydata)
            if (employee_serialize.is_valid()):
                employee_serialize.save() #Update to Db
                return JsonResponse(employee_serialize.data, status=status.HTTP_200_OK)
            else:
                return JsonResponse(employee_serializer.errors,status=status.HTTP_400_BAD_REQUEST)    
            

    except Employee.DoesNotExist: 
        return HttpResponse("Invalid Employee Id", status=status.HTTP_404_NOT_FOUND)

    
            
            
        


@csrf_exempt
def employee_list(request):
    if (request.method == "GET"):
        employees = Employee.objects.all()
        employee_serializer = EmployeeSerializer(employees,many=True)
        return JsonResponse(employee_serializer.data, safe=False)
        

# Create your views here.
@csrf_exempt
def employee_create(request):
    if (request.method == "POST"):

        # getName = request.POST.get("name")
        # getEmployeeCode = int( request.POST.get("empcode") )
        # getEmployeeDesignation = request.POST.get("empdesig")
        # getEmployeeSalary = int(request.POST.get("empsalary") )

        # mydata = {'name': getName, 'empcode': getEmployeeCode, 'empdesig': getEmployeeDesignation, 'empsalary': getEmployeeSalary}
        # mydata=JSONParser().parse(request)
        employee_serialize = EmployeeSerializer(data=request.POST)
        if (employee_serialize.is_valid()):
            employee_serialize.save()  #Save to Db
            return redirect(view_all_employees)
            # return JsonResponse(employee_serialize.data,status=status.HTTP_200_OK)
 
        else:
            return HttpResponse("Error in Serilization",status=status.HTTP_400_BAD_REQUEST)

        
        
       

    else:
        return HttpResponse("GET Method Not Allowed",status=status.HTTP_404_NOT_FOUND)
