from django.shortcuts import render
import apprise
# Create your views here.


def index(request):

    if request.method == "POST":
        s_name = request.POST['r_name']       
        r_name = request.POST['l_name']       
        subject = request.POST['subject']       
        email = request.POST['email']       
        date = request.POST['notificationDate']       
        time = request.POST['notificationTime']       
        msg = request.POST['message']       
        
        apobj = apprise.Apprise()



        title = subject
        body = msg

        apobj.add(f'mailto://mdshurov64:qqacnxsavwtpysyv@gmail.com?to={email}')
        
        apobj.notify(
            title=title,
            body=body,
            # image = body,
            # attach= attach,
        )
    
    return render(request, 'bulk_sms/index.html')