from django.core.cache import cache

from common import keys, stat
from libs.http import render_json
from user.logics import send_vcode

# Create your views here.


def get_vcode(request):
    phonenum=request.GET.get("phonenum")
    if cache.get(keys.VCODE_KEY % phonenum ):
        return render_json(code=stat.OPT_REPEATED)
    send_vcode(phonenum)
    return render_json()


def login(request):

    return render_json()

