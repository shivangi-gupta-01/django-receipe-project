from django.shortcuts import render, redirect
from .models import *


# Create your views here.
def receipes(request):
    # return HttpResponse("heyyyaaaa")
    if request.method == "POST":
        data = request.POST
        receipe_image = request.FILES.get("receipe_Image")
        receipe_name = data.get("receipe_name")
        receipe_description = data.get("receipe_desc")
        # print(receipe_description)
        # print(receipe_name)
        # print(receipe_image)

        Receipe.objects.create(
            receipe_name=receipe_name,
            receipe_description=receipe_description,
            receipe_image=receipe_image,
            )
        return redirect('/receipes/')
    queryset = Receipe.objects.all()
    context={'receipes': queryset}

    return render(request, "receipes.html", context)
