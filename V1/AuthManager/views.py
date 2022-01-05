from django.shortcuts import render
from JWTTokensManager.TokenManager import GenerateToken
from JWTTokensManager.AuthenticationManager import AuthUserManager
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from Exceptions.CustomStringException import EmptyStringException

# Create your views here.
class LoginManager(APIView):
    permission_classes = ( AllowAny,)
    
    def __init__(self) -> None:
        self.req_response={"status":"failed","msg":"authentication failed","data":""}
        

    def post(self,request):

        #check whether user already loggedin
        if request.user.is_authenticated:
            finalResponse={"msg":"already logged in"}
            return Response(finalResponse)
            
        try:
            #read field from request
            username    =   request.data["username"]
            password    =   request.data["password"]

            if username=="":
                raise EmptyStringException("username")
            if password=="":
                raise EmptyStringException("password")

            #authenticate username and password
            user        =   AuthUserManager.authenticate_user(username,password)
            if not user==None:

                #generate token for the user
                token       =   GenerateToken.get_token(user)
                self.req_response={
                    "data" : {
                        "token" : {
                            'access': str(token.access_token),
                            'refresh': str(token),
                        }
                    },
                    "staus":"success",
                    "msg" : "authenticated successfully"
                }
            else:
                self.req_response["data"]="invalid username/password"
                
        except KeyError as e:
            self.req_response["data"]={"required field missing":repr(e)}
        
        except EmptyStringException as e:
            self.req_response["data"]=e.message
        
        except Exception as e:
            # print(e)
            pass

        finally:
            return Response(self.req_response)
