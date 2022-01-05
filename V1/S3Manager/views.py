from botocore.exceptions import ClientError
from django.shortcuts import render
from Exceptions.MediaUploaderException import MediaUploaderException
from FunctionManger.RandomNumberManager import get_random_number_with_datetime
import boto3

class MediaMasterBucket():
    def __init__(self) -> None:
        self.bucket_name          =   "simandhar"

class S3Resource():
    def __init__(self):
        self.region_name            =   'ap-south-1'
        self.aws_access_key_id      =   "AKIASRWMGOFDAQJMGENP"
        self.aws_secret_access_key  =   "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"
        

    def get_s3_resource(self):
        try:
            s3_resource             =   boto3.resource('s3',
            region_name             =   self.region_name,
            aws_access_key_id       =   self.aws_access_key_id,
            aws_secret_access_key   =   self.aws_secret_access_key,

            )
            return s3_resource
        
        except ClientError as e:
            pass
        
        except Exception as e:
            pass


class S3ObjectUploader():
    def __init__(self) -> None:
        pass

    def image_uploader(self,file,destination_path,update=False):
        try:
            file.seek(0)
            s3                          =   S3Resource()
            s3_resource                 =   s3.get_s3_resource()
            file_name,file_extension    =   file.name.split(".")[:-1][0],file.name.split(".")[-1]

            master_bucket               =   MediaMasterBucket().bucket_name

            if not update:
                keyname                 =   get_random_number_with_datetime()+"."+file_extension
                destination_path        =   destination_path+"/"+keyname

            obj                         =   s3_resource.Object(master_bucket,destination_path)    
            resp                        =   obj.put(Body=file.read())
            
            if resp["ResponseMetadata"]["HTTPStatusCode"]==200:
                object_url              =   "https://"+master_bucket+".s3."+s3.region_name+".amazonaws.com/"+destination_path
                return object_url
            
            raise MediaUploaderException()
    
        except Exception as e:
            return e

