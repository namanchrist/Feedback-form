from django.shortcuts import render

from django.shortcuts import render
from .forms import FeedbackForm

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Process the valid data here, no need to store it
            return render(request, 'feedback/thank_you.html', {'form': form})
    else:
        form = FeedbackForm()

    return render(request, 'feedback/feedback_form.html', {'form': form})

