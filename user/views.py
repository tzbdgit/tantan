from django.core.cache import cache
from django.http import JsonResponse

from common import keys, stat
from libs.http import render_json
from user.logics import send_vcode
from user.models import User


def get_vcode(request):
    phonenum=request.GET.get("phonenum")
    if cache.get(keys.VCODE_KEY % phonenum ):
        return render_json(code=stat.OPT_REPEATED)
    send_vcode(phonenum)
    return render_json()


def login(request):
    phonenum=request.POST.get("phonenum")
    vcode=request.POST.get("vcode")
    cache_vcode=cache.get(keys.VCODE_KEY % phonenum)
    if not cache_vcode:
        return render_json(code=stat.VCODE_EXPIRED)
    if vcode==cache_vcode:
        try:
            user=User.objects.get(phonenum=phonenum)
        except User.DoesNotExist:
            user=User.objects.create(phonenum=phonenum,
                                     nickname=phonenum)
        request.session["uid"]=user.id
        # return JsonResponse({"code":0,"data":user.to_dict()})
        return render_json(data=user.to_dict())
    else:
        return render_json(code=stat.VCODE_ERROR)

