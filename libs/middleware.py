from django.utils.deprecation import MiddlewareMixin

from common import stat
from libs.http import render_json
from user.models import User


class AuthMiddleware(MiddlewareMixin):
    API_WHITE_LIST=[
        # "user/get_vcode",
        "user/login"
    ]
    def process_request(self,request):
        print(request.path)
        if request.path not in self.API_WHITE_LIST:
            print("test")
            uid=request.session.get("uid")
            print(uid)
            if not uid:
                return render_json(code=stat.NO_LOGIN)
            else:
                request.user=User.objects.get(id=uid)
