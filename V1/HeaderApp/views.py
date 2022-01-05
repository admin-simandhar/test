from functools import partial
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from Exceptions.CustomStringException import EmptyStringException
from Exceptions.InvalidImageResolution import InvalidImageResolution
from Exceptions.MediaUploaderException import MediaUploaderException
from Exceptions.UnSupportedMedia import UnSupportedMedia
from CloudinaryUploader.views import Uploader
from HeaderApp.models import HeaderBanner
from FunctionManger.DateTimeManager import get_date_time_db
from FunctionManger.MediaHandler import CheckMedia, MediaResolution
from django.db.models import F
from HeaderApp.serializer import HeaderBannerSerializer
from django.conf import settings
from S3Manager.views import S3ObjectUploader                
                
# Create your views here.
class HeaderApp(APIView):
    permission_classes          =   ( AllowAny,)
    
    def __init__(self):
        self.req_response       =   {"status":"failed","msg":"","data":""}
        

    def post(self,request):
        try:
            priority            =   int(request.data["priority"])
            alttag              =   request.data["alttag"]
            
            if priority ==  "":
                raise EmptyStringException("priority")

            if type(priority) is not int:
                raise TypeError("invalid priority type: numeric required")
            
            if alttag   ==  "":
                raise EmptyStringException("alttag")

            media_file          =   request.FILES.get("media", False)
            if not media_file:
                raise EmptyStringException("media")

            else:
                cm              =   CheckMedia(media_file.name)
                if not (cm.isImage() or cm.isVideo()):
                    raise UnSupportedMedia(media_file.name)            

                media_resolution= MediaResolution(settings.IMAGE_MEDIA_RESOLUTIONS["HOME_HEADER_BANNER"])
                media_resolution.checkImage(media_file)


                s3_uploader      =   S3ObjectUploader()
                media_url=s3_uploader.image_uploader(media_file,"header")


                # media_uploader  =   Uploader()
                # media_url       =   media_uploader.upload(media_file)

            
            # update priorities
            HeaderBanner.objects.filter(priority__gte=priority).update(priority=F('priority')+1)

            # Insert into database
            hb                  =   HeaderBanner(alttag=alttag,media_url=media_url,priority=priority,created=get_date_time_db(),updated=get_date_time_db())
            hb.save()

            self.req_response["status"] =   "success"
            self.req_response["msg"]    =   "added successfully"
            
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
            # import traceback,sys
            # traceback.print_exc()
        return Response(self.req_response)
    
    def get(self,request):        
        try:        
            header_banners              =   HeaderBannerSerializer(HeaderBanner.objects.all().order_by('priority'),many=True)
            self.req_response["data"]   =   header_banners.data
            self.req_response["status"] =   "success"
            self.req_response["msg"]    =   "data retirved successfully"
        except Exception as e:
            pass
        return Response(self.req_response)
        
    def put(self,request):
        try:
            hb=HeaderBanner.objects.get(id=request.data["id"])
            params=request.data

            media_url       =   ""
            if "media" in list(request.data.keys()):
                media_file          =   request.FILES.get("media", False)
                if not media_file:
                    raise EmptyStringException("media")
                    
                cm      =   CheckMedia(media_file.name)
                if not (cm.isImage() or cm.isVideo()):
                    raise UnSupportedMedia(media_file.name)            

                media_resolution            =   MediaResolution(settings.IMAGE_MEDIA_RESOLUTIONS["HOME_HEADER_BANNER"])
                media_resolution.checkImage(media_file)

                media_url_old               =   hb.media_url.split("amazonaws.com/")[1]
                
                s3_uploader                 =   S3ObjectUploader()
                media_url                   =   s3_uploader.image_uploader(media_file,media_url_old,update=True)

            
            if media_url!="":
                params["media_url"]         =   media_url
            
            if "priority" in list(request.data.keys()):
                # update priorities
                HeaderBanner.objects.filter(priority__gte=params["priority"]).update(priority=F('priority')+1)

            params["updated"]               =   get_date_time_db()
            hs=HeaderBannerSerializer(hb,data=params,partial=True)

            if hs.is_valid():
                hs.save()
                self.req_response["status"] =   "success"
                self.req_response["msg"]    =   "updated successfully"
            else:
                self.req_response["data"]   =   hs.errors


        except EmptyStringException as e:
            self.req_response["data"]       =   e.message

        except UnSupportedMedia as e:
            self.req_response["data"]       =   e.message

        except MediaUploaderException:
            self.req_response["msg"]        =   "update failed"
            self.req_response["data"]       =   "failed to upload media"

        except HeaderBanner.DoesNotExist:
            self.req_response["msg"]        =   "invalid id"
            self.req_response["data"]       =   "update failed"

        except InvalidImageResolution as iir:
            self.req_response["msg"]        =   "invalid media size/resolution"
            self.req_response["data"]       =   iir.message

        except Exception as e:
            # print(e)
            self.req_response["msg"]        =   "ERROR"
            import traceback
            traceback.print_exc()
        return Response(self.req_response)
        
    
    def delete(self,request):
        
        try:
            hb=HeaderBanner.objects.get(id=request.data["id"])
            hb.delete()
            self.req_response["status"]     =   "success"
            self.req_response["msg"]        =   "deleted successfully"
        
        except HeaderBanner.DoesNotExist:
            self.req_response["msg"]        =   "failed to delete"
            self.req_response["data"]       =   "invalid id"
        
        except Exception:
            self.req_response["msg"]        =   "ERROR: DELETE"

        return Response(self.req_response)
        
        