from json import dumps

from django.http import HttpResponse

from tantan import settings


def render_json(code=0,data=None):
    result={
        "code":code,
        "data":data
    }
    if settings.DEBUG:
        json_str=dumps(result,ensure_ascii=False,
                       sort_keys=True,indent=4)
    else:
        json_str=dumps(result,ensure_ascii=False,
                       separators=[",",":"])
    return HttpResponse(json_str)