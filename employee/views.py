from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from employee.serializers import EmployeeSerializer
from employee.models import Employee
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests




@csrf_exempt
def Delete_Search_api(request):
    try:
        getEmpCode = request.POST.get("empcode")
        getEmployee = Employee.objects.filter(empcode=getEmpCode)
        employee_serialiser = EmployeeSerializer(getEmployee, many=True)
        return render(request,"delete.html",{"data":employee_serialiser.data})
        # return JsonResponse(employee_serialiser.data,safe=False,status=status.HTTP_200_OK)

    except Employee.DoesNotExist:
        return HttpResponse("Invalid Emp Code", status=status.HTTP_404_NOT_FOUND)
        
    except:
        return HttpResponse("Something went wrong")    


@csrf_exempt
def employee_details_deletebtn(request):


    newId = request.POST.get("newId")
   
    setUrl="http://localhost:8000/employee/viewemployee/"+newId
    requests.delete(setUrl)
    return HttpResponse("Deleted")


@csrf_exempt
def Update_Search_api(request):
    try:
        getEmpCode = request.POST.get("empcode")
        getEmployee = Employee.objects.filter(empcode=getEmpCode)
        employee_serialiser = EmployeeSerializer(getEmployee, many=True)
        return render(request,"update.html",{"data":employee_serialiser.data})
        # return JsonResponse(employee_serialiser.data,safe=False,status=status.HTTP_200_OK)

    except Employee.DoesNotExist:
        return HttpResponse("Invalid Emp Code", status=status.HTTP_404_NOT_FOUND)
        
    except:
        return HttpResponse("Something went wrong")    


@csrf_exempt
def employee_details_updatebtn(request):


    getName = request.POST.get("newname")
    newId = request.POST.get("newId")
    newempsalary = request.POST.get("newempsalary")
    newempcode = request.POST.get("newempcode")
    getEmployeeDesignation = request.POST.get("newempdesig")

    mydata = {'name': getName, 'empdesig': getEmployeeDesignation,'empcode': newempcode,'empsalary': newempsalary}
    jsondata=json.dumps(mydata)
    print(jsondata)
   
    setUrl="http://localhost:8000/employee/viewemployee/"+newId
    requests.put(setUrl, data=jsondata)
    return HttpResponse("Updated")

@csrf_exempt
def employee_details_delete(request):


    try:

        getEmpCode = int(request.POST.get("empid"))
        print(getEmpCode)
        employees = Employee.objects.get(id=getEmpCode)
        if (request.method == "POST"):
            employees.delete()
            return HttpResponse("Deleted", status=status.HTTP_204_NO_CONTENT)
    except:
        return HttpResponse("Invalid Emp Code", status=status.HTTP_404_NOT_FOUND)



def search_view_employees(request):
    return render(request, 'search.html')


@csrf_exempt
def searchapi(request):
    try:
        getEmpCode = request.POST.get("empcode")
        getEmployee = Employee.objects.filter(empcode=getEmpCode)
        employee_serialiser = EmployeeSerializer(getEmployee, many=True)
        return render(request,"search.html",{"data":employee_serialiser.data})
        # return JsonResponse(employee_serialiser.data,safe=False,status=status.HTTP_200_OK)

    except Employee.DoesNotExist:
        return HttpResponse("Invalid Emp Code", status=status.HTTP_404_NOT_FOUND)
        
    except:
        return HttpResponse("Something went wrong")    

def delete_view_employees(request):
    return render(request, 'delete.html')
    
def update_view_employees(request):
    return render(request, 'update.html')
    
def view_all_employees(request):

    fetchdata=requests.get("https://mydjangotestapp1.herokuapp.com/employee/viewall/").json()

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
            # print(request.PUT)
            # getName = request.PUT.get("name")
           
            # getEmployeeDesignation = request.PUT.get("empdesig")
        

            # mydata = {'name': getName,'empdesig': "fg",'empcode': '1001','empsalary': 0}
            mydata=JSONParser().parse(request)
            print(mydata)
            # mydata=JSONParser().parse(request)
            employee_serialize = EmployeeSerializer(employees,data=mydata)
            if (employee_serialize.is_valid()):
                employee_serialize.save() #Update to Db
                return JsonResponse(employee_serialize.data, status=status.HTTP_200_OK)
            else:
                return JsonResponse(employee_serialize.errors,status=status.HTTP_400_BAD_REQUEST)    
            

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
