from django.shortcuts import render
import requests, json

# Create your views here.
def home(request):

    response = requests.get("http://www.boredapi.com/api/activity/")
    #data = json.loads(response)
    # create a formatted string of the Python JSON object
    text = json.dumps(response.json(), sort_keys=True, indent=4)
    text_1 = json.loads(text)
    
    if "activity" in text_1:
        print(True)
    else:
        print(False)

    return render(request, 'html-static/index.html', {'result': text_1["type"]})