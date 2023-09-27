from textwrap import wrap
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect

#decorator untuk membatasi role apa saja yang boleh mengakses view
def role_required(allowed_roles=[]):
    def decorator(view_function):
        def wrapper(request, *args, **kwargs):
            if request.user.is_staff or request.user.role in allowed_roles:
                return  view_function(request, *args, **kwargs)
            else:
                raise PermissionDenied
        return wrapper
    return decorator

#decorator untuk mengecek apakah user sudah verifikasi email
def is_verified():
    def decorator(view_function):
        def wrapper(request, *args, **kwargs):
            if request.user.is_verified:
                return view_function(request, *args, **kwargs)
            else:
                return redirect('profile:admin_verification',)
        return wrapper
    return decorator