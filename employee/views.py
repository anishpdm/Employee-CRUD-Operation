from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from employee.serializers import EmployeeSerializer
from employee.models import Employee
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests


def deleteemployeescreen(request):
    return render(request,"delete.html")

@csrf_exempt
def delete_data_read(request):
    
    getnewid = request.POST.get("newid")
    getnewempcode=request.POST.get("newempcode")
    getnewsalary=request.POST.get("newsalary")
    getnewdesig = request.POST.get("newdesig")
    getName = request.POST.get("newname")
    mydata = {'name': getName, 'empcode': getnewempcode, 'empdesig': getnewdesig, 'empsalary': getnewsalary,'status':0}
    jsondata=json.dumps(mydata)
    ApiLink = "http://localhost:8000/employee/viewemployee/" + getnewid
    x = requests.put(ApiLink, data=jsondata)
    print(x)
    return HttpResponse("Data has deleted succesfully")
    
    


@csrf_exempt
def delete_search_api(request):
    try:
        
        getEmployeeCode = int( request.POST.get("empcode") )
        employees = Employee.objects.get(empcode=getEmployeeCode)
        employee_serializer = EmployeeSerializer(employees)
        return render(request,'delete.html',{"data":employee_serializer.data})
        # return JsonResponse(employee_serializer.data, safe=False, status=status.HTTP_200_OK)

    except Employee.DoesNotExist: 
        return HttpResponse("Invalid Employee Id", status=status.HTTP_404_NOT_FOUND)
    



@csrf_exempt
def update_data_read(request):
    
    getnewid = request.POST.get("newid")
    
    getnewempcode=request.POST.get("newempcode")
    getnewsalary=request.POST.get("newsalary")
    getnewdesig = request.POST.get("newdesig")
    getName = request.POST.get("newname")
    mydata = {'name': getName, 'empcode': getnewempcode, 'empdesig': getnewdesig, 'empsalary': getnewsalary}
    jsondata=json.dumps(mydata)
    ApiLink = "http://localhost:8000/employee/viewemployee/" + getnewid
    requests.put(ApiLink, data=jsondata)
    return HttpResponse("Data has updated succesfully")
    
    


@csrf_exempt
def update_search_api(request):
    try:
        
        getEmployeeCode = int( request.POST.get("empcode") )
        employees = Employee.objects.get(empcode=getEmployeeCode)
        employee_serializer = EmployeeSerializer(employees)
        return render(request,'update.html',{"data":employee_serializer.data})
        # return JsonResponse(employee_serializer.data, safe=False, status=status.HTTP_200_OK)

    except Employee.DoesNotExist: 
        return HttpResponse("Invalid Employee Id", status=status.HTTP_404_NOT_FOUND)
    

@csrf_exempt
def searchapi(request):
    try:
        
        getEmployeeCode = int( request.POST.get("empcode") )
        employees = Employee.objects.get(empcode=getEmployeeCode)
        employee_serializer = EmployeeSerializer(employees)
        return render(request,'search.html',{"data":employee_serializer.data})
        # return JsonResponse(employee_serializer.data, safe=False, status=status.HTTP_200_OK)

    except Employee.DoesNotExist: 
        return HttpResponse("Invalid Employee Id", status=status.HTTP_404_NOT_FOUND)
    
       

def search_view_employees(request):

    return render(request,'search.html')

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
        employees = Employee.objects.filter(status=1)
        employee_serializer = EmployeeSerializer(employees,many=True)
        return JsonResponse(employee_serializer.data, safe=False)
        

# Create your views here.
@csrf_exempt
def employee_create(request):
    if (request.method == "POST"):

        employee_serialize = EmployeeSerializer(data=request.POST)
        if (employee_serialize.is_valid()):
            employee_serialize.save()  #Save to Db
            return redirect(view_all_employees)
            # return JsonResponse(employee_serialize.data,status=status.HTTP_200_OK)
 
        else:
            return HttpResponse("Error in Serilization",status=status.HTTP_400_BAD_REQUEST)

        
        
       

    else:
        return HttpResponse("GET Method Not Allowed",status=status.HTTP_404_NOT_FOUND)
