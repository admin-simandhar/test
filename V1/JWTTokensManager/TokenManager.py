from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.exceptions import AuthenticationFailed, InvalidToken, TokenError
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.authentication import JWTAuthentication
from JWTTokensManager.AuthenticationManager import AuthUserManager
from rest_framework.permissions import BasePermission


class GenerateToken(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls,user):    
        token = super().get_token(user)        
        return token


class JWTTokenUserAuthenticationService(JWTAuthentication):
    def get_user(self, validated_token):
        try:
            user_id =   validated_token[api_settings.USER_ID_CLAIM]
            u       =   AuthUserManager.user_exist(user_id)
            if u==None:
                raise AuthenticationFailed(_('Invalid User'))
            else:
                u.is_authenticated=True
                u.id=user_id
            return u
        except KeyError:
            raise InvalidToken(_('Token contained no recognizable user identification'))
        except:
            raise TokenError

# class SuperAdminPermissionClass(BasePermission):
#     def has_permission(self, request, view):
#         return AuthUserManager.is_super_admin(request.user.id)