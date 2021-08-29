from django.core.exceptions import PermissionDenied
from  .models import StudentProfile


def prime_user(function):
    def wrap(request, *args, **kwargs):
        user = request.user
        student = StudentProfile.objects.get(user=user)
        if student.prime_user == True:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap