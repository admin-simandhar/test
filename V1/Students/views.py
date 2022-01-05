from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializer import StudentsSerializer,StudentsCourseSerializer
from Exceptions.CustomStringException import EmptyStringException
from Exceptions.InvalidImageResolution import InvalidImageResolution
from Exceptions.UnSupportedMedia import UnSupportedMedia
from FunctionManger.MediaHandler import CheckMedia, MediaResolution
from S3Manager.views import S3ObjectUploader     
from django.conf import settings
# Create your views here.
class Student(APIView):
    permission_classes          =   ( AllowAny,)
    
    def __init__(self):
        self.req_response       =   {"status":"failed","msg":"","data":""}

    def post(self,request):
        try:

            data                        =   request.data
            profile_img                 =   request.FILES.get("profile_img", False)

            if not profile_img:
                raise EmptyStringException("media")

            else:
                cm                      =   CheckMedia(profile_img.name)
                if not (cm.isImage() or cm.isVideo()):
                    raise UnSupportedMedia(profile_img.name)            

                media_resolution        =   MediaResolution(settings.IMAGE_MEDIA_RESOLUTIONS["STUDENT_PROFILE_IMG"])
                media_resolution.checkImage(profile_img)

                s3_uploader             =   S3ObjectUploader()
                profile_img_url         =   s3_uploader.image_uploader(profile_img,"students")
                
                data["profile_img"]     =   profile_img_url

            students_serializer         =   StudentsSerializer(data=data)
            students_serializer.is_valid(raise_exception=True)
            students_serializer.save()
            self.req_response["data"]   ="success"
            self.req_response["msg"]    ="student created successfully"

        except UnSupportedMedia as e:
            self.req_response["data"]   =   e.message
            
        except KeyError as e:
            self.req_response["data"]   =   {"required field missing":repr(e)}
        
        except ValueError as e:
            print(e)
            self.req_response["data"]   =   "numeric required: priority"

        except EmptyStringException as e:
            print(e)
            self.req_response["data"]   =   e.message

        except InvalidImageResolution as iir:
            self.req_response["msg"]    =   "invalid media size/resolution"
            self.req_response["data"]   =   iir.message
        
        except Exception as e:
            print(e.__class__)
            import traceback,sys
            traceback.print_exc()

        return Response(self.req_response)


class StudentCourse(APIView):
    permission_classes          =   ( AllowAny,)
    
    def __init__(self):
        self.req_response       =   {"status":"failed","msg":"","data":""}

    def post(self,request):
        d=request.data
        sc=StudentsCourseSerializer(data=d)
        sc.is_valid(raise_exception=True)
        sc.save()
        return Response({})

class StudentPlacement(APIView):
    permission_classes          =   ( AllowAny,)
    
    def __init__(self):
        self.req_response       =   {"status":"failed","msg":"","data":""}

    def post(self,request):
        d=request.data
        sc=StudentsCourseSerializer(data=d)
        sc.is_valid(raise_exception=True)
        sc.save()
        return Response({})
