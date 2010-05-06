import django.dispatch

user_logged_in = django.dispatch.Signal(providing_args=['request', 'user'])
user_logged_out = django.dispatch.Signal(providing_args=['request',])
