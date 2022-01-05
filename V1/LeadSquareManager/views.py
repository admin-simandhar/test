from django.shortcuts import render
import requests
from rest_framework.exceptions import ValidationError
# Create your views here.
class LeadSquareManager():

    def __init__(self) -> None:
        self.access_key="u$r2c120281f743fabc884c3570faf4e10c"
        self.secret_key="15dc1fbf7374fe87461f75af120971d5146c3728"
    
    def getLeadSquareFieldMappers(self):
        lead_square_field_mappers = {
            "firstname"     :   "FirstName",
            "lastname"      :   "LastName",
            "email"         :   "EmailAddress",
            "phone"         :   "Phone",
            "select_course" :   "mx_Course",
            "qualification" :   "mx_Qualification"
        }
        return lead_square_field_mappers

    def setLeadSquareFields(self,lead_info):
        lead_data       =   []
        lead_square_field_mappers = self.getLeadSquareFieldMappers()
        for lk,lv in lead_info.items():
            if lk in list(lead_square_field_mappers.keys()):
                lead_data.append({"Attribute":lead_square_field_mappers[lk],"Value":lv})
        return lead_data
        
    def createLead(self,lead_data):
        req_url         =   "https://api-in21.leadsquared.com/v2/LeadManagement.svc/Lead.Create?accessKey="+self.access_key+"&secretKey="+self.secret_key
        headers         =   {"Content-Type": "application/json"}
        lead_data       =   self.setLeadSquareFields(lead_data)
        response        =   requests.post(req_url,headers=headers,json=lead_data)
        print(response)

        if response.status_code == 200:
            return True
        elif response.status_code==500:
            ee=response.json()
            raise ValidationError({"lead duplication error in lead square":ee["ExceptionMessage"]})
        return False