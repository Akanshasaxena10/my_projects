from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse


monthly_challenges_variable = {
    "january":"Eat no rice for 3 months!",
    "february":"Walk for at least 20 minutes every day!",
    "march":"Walk for at least 20 minutes every day!",
    "april":"Go to sleep before 10pm everyday!",
    "may" : "Don't forget to take your me time daily",
    "june" : "Travel plan for the next six months!",
    "july" : "Read one book this month!",
    "august" : "Please visit your relatives this month!",
    "september" :"This month complete the pending works!",
    "october" : "This is a festival month....Enjoy!",
    "november": "Try to list out all you completed,pending tasks!",
    "december" : "Make new plans for the new year and enjoy christmas!!!!!!!"                             
}  

def index(request):
    # list_items=""
    months=list(monthly_challenges_variable.keys())
    
    return render(request, "challenges/index.html",{
        "month": months
        })
    
    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path =reverse("month-challenge",args=[month])
    #     list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)
    # """
    # <ul>
    #    <li><a> href="/challenges/january">January</a></li>
    #    <li><a> href="/challenges/february">February</a></li>
    #    <li><a> href="/challenges/march">March</a></li>
    #    <li><a> href="/challenges/april">April</a></li>
    #    <li><a> href="/challenges/may">May</a></li>
    #    <li><a> href="/challenges/june">June</a></li>
    #    <li><a> href="/challenges/july">July</a></li>
    #    <li><a> href="/challenges/august">August</a></li>
    #    <li><a> href="/challenges/september">September</a></li>
    #    <li><a> href="/challenges/october">October</a></li>
    #    <li><a> href="/challenges/november">November</a></li>
    #    <li><a> href="/challenges/december">December</a></li>
    #    </ul>
    # """
   

def monthly_challenge_number(request,month):###if months are in numbers
    months = list(monthly_challenges_variable.keys())###converting a dictionary into list with inbuilt key function.
    
    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid Month</h1>")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge",args=[redirect_month])##/challenges/month-name
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request,month):####dynamic function
    try:
        challenge_text = monthly_challenges_variable[month]
        return render(request,"challenges/challenge.html",{
            "text": challenge_text,
            "month_name":month###to have dynamic response in templates
        })
        
        # response_data = render_to_string("challenges/challenge.html")###we can replace it with render short cut
        # return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!!!!</h1>")  
# # Create your views here.
# def january(request):##function
#     return HttpResponse("Eat no rice for 3 months!")##instantiating a class

# def february(request):
#     return HttpResponse("Walk for at least 20 minutes every day!")

# def march(request):
#     return HttpResponse("Walk for at least 20 minutes every day!")

# def april(request):
#     return HttpResponse("Go to sleep before 10pm everyday!")

# def may(request):
#     return HttpResponse("Don't forget to take your me time daily!")

# def june(request):
#     return HttpResponse("Travel plan for the next six months!")

# def july(request):
#     return HttpResponse("Read one book this month!")

# def august(request):
#     return HttpResponse("Pease visit your relatives this month!")

# def september(request):
#     return HttpResponse("This month complete the pending works!")

# def october(request):
#     return HttpResponse("This is a festival month....Enjoy!")

# def november(request):
#     return HttpResponse("Try to list out all you completed,pending tasks!")

# def december(request):
#     return HttpResponse("Make new plans for the new year and enjoy christmas!!!!!!!")

   
    


# def monthly_challenge(request,month):####dynamic function
#     challenge_text = None
#     if month == "january":
#         challenge_text = "Eat no rice for 3 months!"
#     elif month == "february":
#         challenge_text = "Walk for at least 20 minutes every day!"
#     elif month == "march":
#         challenge_text = "Drink 5 liters of water daily!"
#     elif month == "april":
#         challenge_text = "Go to sleep before 10pm everyday!"
#     elif month == "may":
#         challenge_text = "Don't forget to take your me time daily!"
#     elif month == "june":
#         challenge_text = "Travel plan for the next six months!" 
#     elif month == "july":
#         challenge_text = "Read one book this month!"          
#     elif month == "august":
#         challenge_text = "Pease visit your relatives this month!"          
#     elif month == "september":
#         challenge_text = "This month complete the pending works!"
#     elif month == "october":
#         challenge_text = "This is a festival month....Enjoy!"
#     elif month == "november":
#         challenge_text = "Try to list out all you completed,pending tasks!"
#     elif month == "december":
#         challenge_text = "Make new plans for the new year and enjoy christmas!!!!!!!"   
#     else:
#         return HttpResponseNotFound("This month is not supported!!")
#     return HttpResponse(challenge_text)   
