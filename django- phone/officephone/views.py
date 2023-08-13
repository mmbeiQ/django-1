from django.shortcuts import render,HttpResponse


# Create your views here.

 def home(request):
      return HttpResponse(خوش آمدید"")

def etelaat(request):
    l=[
       {"onvan":"fani", "tozihat":"سازمان فنی حرفه ای", "phone":"118-01"}
       {"onvan":"kar", "tozihat":"سازمان کار و رفاه", "phone":"118-02"}
       {"onvan":"tamin", "tozihat":"سازمان تامین اجتماعی", "phone":"118-03"}
       {"onvan":"uni", "tozihat":"دانشگاه", "phone":"118-04"}
    ]
    d=l[0]
     for i in l:
        if (esm==i["onvan"]):d=i
            return render(request,"officephone/show.html",context=d)
    
    return HttpResponse("officephone/show.html")
 

      
    
