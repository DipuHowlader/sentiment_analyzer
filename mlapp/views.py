from django.shortcuts import render
from .utils import load_model
from datetime import date

model = load_model()

user_text = ["life  is good "]
today_date = date.today().strftime("%B %d, %Y")


def home(request):
    if request.method == 'POST':
        user_text = request.POST.get('user_input')
        predictions = model.predict([user_text])
        return render(request, 'mlapp/predict.html', { 'prediction': predictions[0], 'today_date': today_date})

    return render(request, 'mlapp/home.html', {'today_date': today_date})
