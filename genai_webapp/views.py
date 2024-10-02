# genai_webapp/views.py

from django.shortcuts import render
from .forms import CodeUploadForm, QuizUploadForm
from .genai.socratic_ai import socratic_guidance
from .models import UserSubmissions, AIResponses
from django.http import JsonResponse

# Home page view
def home(request):
    return render(request, 'home.html')

# Chat view for the result page (handles real-time chat responses)
def result_chat_view(request):
    if request.method == 'POST':
        user_message = request.POST.get('user_message', '')
        
        # Get Socratic guidance from the AI for the latest user input
        ai_response = socratic_guidance(user_message)
        
        # Return the AI's response as JSON (for AJAX)
        return JsonResponse({'ai_response': ai_response})

# Handle interactive chat for code or quiz
def chat_view(request):
    if request.method == 'POST':
        user_message = request.POST.get('user_message', '')
        
        # Get Socratic guidance from the AI for the latest user input
        ai_response = socratic_guidance(user_message)
        
        # Return the AI's response as JSON (for AJAX)
        return JsonResponse({'ai_response': ai_response})
    
    # Render the chat interface template
    return render(request, 'chat_interface.html')

def upload_code(request):
    if request.method == 'POST':
        form = CodeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Get code from form
            code_file = form.cleaned_data['code_file'].read().decode('utf-8')
            
            # Save code submission to database
            submission = UserSubmissions.objects.create(submission_type='code', content=code_file)
            
            # Process code through Socratic AI guidance
            guidance = socratic_guidance(code_file)
            
            # Save AI response to database
            AIResponses.objects.create(submission=submission, ai_response=guidance)
            
            # Render response to user
            return render(request, 'result.html', {'guidance': guidance})
    else:
        form = CodeUploadForm()

    return render(request, 'upload_code.html', {'form': form})

def upload_quiz(request):
    if request.method == 'POST':
        form = QuizUploadForm(request.POST)
        if form.is_valid():
            # Get quiz content from form
            quiz_text = form.cleaned_data['quiz_text']
            
            # Save quiz submission to database
            submission = UserSubmissions.objects.create(submission_type='quiz', content=quiz_text)
            
            # Process quiz through Socratic AI guidance
            guidance = socratic_guidance(quiz_text)
            
            # Save AI response to database
            AIResponses.objects.create(submission=submission, ai_response=guidance)
            
            # Render response to user
            return render(request, 'result.html', {'guidance': guidance})
    else:
        form = QuizUploadForm()

    return render(request, 'upload_quiz.html', {'form': form})
