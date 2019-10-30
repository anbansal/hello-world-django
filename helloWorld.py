import sys
from django.conf import settings
from django.conf.urls import include,url
from django.http import HttpResponse
from django.core.management import execute_from_command_line

settings.configure(
    DEBUG = True,
    SECRET_KEY = 'letsseeifthiskeycanwork',
    ROOT_URLCONF=sys.modules[__name__],
)


def index(reques):
    return HttpResponse("Hello World!!!")

urlpatterns = [
    url('',index),
    url('^$',index),
    url(r'^hello-world/$',index),
]


if __name__ == "__main__":
    execute_from_command_line(sys.argv)
