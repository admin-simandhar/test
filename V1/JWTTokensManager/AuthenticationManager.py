from User.models import User as AuthUser
from HashAlgo.views import getHashSha256
class AuthUserManager():

    def is_super_admin(user_id):
        try:
            u=AuthUser.objects.get(id=user_id)
            if u.is_super_admin:
                return True
            return False
        except:
            return False
            
    def is_user_exist(user_id):
        try:
            AuthUser.objects.get(id=user_id)
            return True
        except:
            return False

    def user_exist(user_id):
        try:
            user=AuthUser.objects.get(id=user_id)
            return user
        except:
            return None

    def authenticate_user(username,password):
        try:
            password = getHashSha256(password)
            user=AuthUser.objects.get(username=username,password=password)
            return user
        except:
            return None
