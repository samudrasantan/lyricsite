from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.shortcuts import render
import datetime

def date_time(request):
    time = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)
    

def hello(request):
    return HttpResponse("Hello world")

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now()+datetime.timedelta(hours=offset)
    html= "<html><body>in %s hours it will be %s</body></html>" % (offset, dt)
    return HttpResponse(html)

def index_artist(request):
    return render(request,'index.html',{'title':[1,2,3,4,5,6,7,8,9,10], 'value':[1,2,3]})

def url(request):
    all_meta = request.META.items()
    all_meta.sort()
    meta_list = []
    for a, b in all_meta:
        meta_list.append("<tr><td>name: %s</td><td>values: %s</td></tr>" % (a, b))
    return HttpResponse("<table>%s</table>" % '\n'.join(meta_list))

from mysite.forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(initial={'subject': 'I love your site!'})
    return render(request, 'contact_form.html', {'form': form})
