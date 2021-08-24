from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from company.company_serializer import CompanySerializer
from django.http import HttpResponse, JsonResponse

# Create your views here.


@csrf_exempt
def add_company(request):
    if (request.method == "POST"):
        getCname=request.POST.get("cname")
        getCaddress=request.POST.get("caddress")
        getCmobile = request.POST.get("cmobile")
        mydata = {"cname": getCname, "caddress": getCaddress, "cmobile": getCmobile}
        company_serialise = CompanySerializer(data=mydata)
        if (company_serialise.is_valid()):
            company_serialise.save()
            return JsonResponse(company_serialise.data)
        else:
            return HttpResponse("Error in Serialisation")    
     
