from django.http import HttpResponse

# Create your views here.
def hello_view(request):
    print(request.COOKIES)

    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    if num_visits > 4:
        del(request.session['num_visits'])

    old_value = request.COOKIES.get('foo', None)
    response = HttpResponse(
        'Cookie value is ' + str(old_value) +
        '<br>num_visits is ' + str(num_visits))
    
    if old_value is not None:
        response.set_cookie('foo', int(old_value) + 1)
    else:
        response.set_cookie('foo', 1)
    response.set_cookie('dj4e_cookie', '064c0ef4', max_age=1000)
