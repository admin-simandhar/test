import mimetypes
from PIL import Image
from Exceptions.InvalidImageResolution import InvalidImageResolution

class CheckMedia():
    def __init__(self,filename):
        mimetypes.init()
        self.mimestart = mimetypes.guess_type(filename)[0]
        if self.mimestart != None:
            self.mimestart = self.mimestart.split('/')[0]

        
    def isImage(self):
        if self.mimestart=="image":
            return True
        return False

    def isVideo(self):
        if self.mimestart=="video":
            return True
        return False        

    def isAudio(self):
        if self.mimestart=="audio":
            return True
        return False



class MediaResolution():
    def __init__(self,image_proporties):
        
        self.aspect_ratio_width = image_proporties["aspect_ratio_width"]
        self.aspect_ratio_height = image_proporties["aspect_ratio_height"]

        self.min_width  = image_proporties["min_width"]
        self.min_height = image_proporties["min_height"]

        self.max_width  = image_proporties["max_width"]
        self.max_height = image_proporties["max_height"]  
    
    def checkImage(self,media_file):
        media_file.seek(0)
        img = Image.open(media_file)
        
        img_width, img_height = img.size

        if (img_width>=self.min_width and img_width<=self.max_width) and (img_height >= self.min_height and img_height<=self.max_height):
            expected_img_height=int(img_width*self.aspect_ratio_height/self.aspect_ratio_width)
            if expected_img_height==img_height:
                return True
            else:
                raise InvalidImageResolution("invalid ratio: "+str(self.aspect_ratio_width)+":"+str(self.aspect_ratio_height))
        else:
            raise InvalidImageResolution("invalid image size. expected:- min: "+str(self.min_width)+"x"+str(self.min_height)+"  max: "+str(self.max_width)+"x"+str(self.max_height))
        