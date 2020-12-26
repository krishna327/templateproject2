from django.shortcuts import render
import datetime
# Create your views here.

def wish(request):
    date = datetime.datetime.now()
    msg = 'Hello Guest !!! very very Good'
    h=int(date.strftime('%H'))
    if h<12:
        msg+='Morning'
    elif h<16:
        msg+='Afternoon'
    elif h<21:
        msg+='Evening'
    else:
        msg+='Good Night'
    my_dict={'insert_date':date,'insert_msg':msg}
    return render(request,'testApp/results.html',context=my_dict)


