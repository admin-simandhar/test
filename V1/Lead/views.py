from django.shortcuts import render
from rest_framework import response
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from LeadSquareManager.views import LeadSquareManager
from .models import Leads
from .serializer import LeadsSerializer
from FunctionManger.DateTimeManager import get_date_time_db
import requests
# Create your views here.
class Leadmg(APIView):
    permission_classes = ( AllowAny,)
    
    def __init__(self) -> None:
        self.req_response={"status":"failed","msg":"failed to create lead","data":""}
        
    def post(self,request):
        try: 
            lead_data                   =   request.data["lead_data"]
            lead_data["created"]        =   get_date_time_db()
            leads                       =   Leads()
            leads_serializer            =   LeadsSerializer(leads,data=lead_data,partial=True)
            
            leads_serializer.is_valid(raise_exception=True)
            
            leads_serializer.save()

            # to insert leads into leadsquare
            
            lsm     =   LeadSquareManager()
            if lsm.createLead(lead_data):
                lead_data["ls_record"]  =   True
                leads_serializer_update =   LeadsSerializer(leads,data=lead_data,partial=True)
                leads_serializer_update.is_valid()
                leads_serializer_update.save()
            

            # to print Quereies
            # from django.db import connection
            # print(connection.queries)


            self.req_response["status"] = "success"
            self.req_response["msg"] = "lead created successfully"


        except ValidationError as e:
            self.req_response["data"]=e.args
            return Response(self.req_response) 
        
        except Exception as e:
            import traceback
            print(traceback.format_exc())
            print(e.__traceback__)
            print(e.__class__)

        return Response(self.req_response)

    def get(self,request):
        c=LeadsSerializer(Leads.objects.all(),many=True)
        return Response(c.data)
