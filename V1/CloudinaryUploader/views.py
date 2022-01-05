from django.shortcuts import render
import cloudinary
import cloudinary.uploader
from FunctionManger.RandomNumberManager import get_random_number_with_datetime
from Exceptions.MediaUploaderException import MediaUploaderException
from PIL import Image
class Uploader():
    def __init__(self):
        cloudinary.config( 
            cloud_name      =   "dp6jcqdpm", 
            api_key         =   "315596631181147", 
            api_secret      =   "qU1EkzirCcdxvp6a0bhL3DVsqrw",
            secure          =   True
        )


    def upload(self,file):
        try:
            file.seek(0)
            public_id       =   get_random_number_with_datetime()
            cresponse       =   cloudinary.uploader.upload(file, 
                                    folder = "Simandhar/header/", 
                                    public_id = public_id,
                                    overwrite = True, 
                                )
            return cresponse["secure_url"]
        except:
            raise MediaUploaderException()
