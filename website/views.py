from django.shortcuts import render, HttpResponseRedirect, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from accounts.models import Profile
from .models import Question, Python, Solved
from .forms import AnswerForm
from django.contrib.auth.decorators import login_required
from website.filehelper.uniquename import get_unique_file_name
from django.contrib import messages
import os
import shutil

# Create your views here.

#questions
@login_required
def question(request):
    if request.user.is_authenticated:
        pi = Question.objects.all()
        return render(request, 'questions.html', {'ques':pi})
    else:
        return HttpResponseRedirect('/login/')

#Solution area
@login_required
def view_question(request, qid):
    pi = Question.objects.get(pk=qid)
    form = AnswerForm()
    context = {
            'Qno': pi.qid,
            'Name': pi.question_title,
            'Question': pi.question_text,
            'Points': pi.points,
            'form': form,
            'message1': 'there is an error in code please check it.'
        }
    if request.method =='POST':
        filename = get_unique_file_name()
        ImageID = get_unique_file_name()
        folder = os.mkdir('code/'+filename)
        form = AnswerForm(request.POST)
        if form.is_valid():
            fh = open ('code/' + filename +'/code.py', 'w+')
            fh.write(form.cleaned_data['Code'])
            fh.close()
            ft = open('code/'+filename+'/test.py','w+')
            ft.write(pi.python.test)
            ft.close()
            fc = open ('code/' + filename + '/Dockerfile', 'w+')
            fc.write('FROM python:alpine\n'+
            'RUN mkdir /python\n'+
            'COPY . /python\n'+
            'WORKDIR /python\n'+
            'CMD ["python", "test.py"]')
            fc.close()
            os.system('cd /home/akhil/Alphacoders/code/'+filename+';docker build . -t '+filename+':'+filename)
            print("build success")
            os.system('cd /home/akhil/Alphacoders/code/'+filename+';docker run --name '+ImageID+' -it '+filename+':'+filename)
            print("run")
            os.system('cd /home/akhil/Alphacoders/code/'+filename+';docker cp '+ImageID+':/python/answers.txt .')
            os.system('cd /home/akhil/Alphacoders/code/'+filename+';docker ps --filter status=exited -q | xargs docker rm')
            os.system('cd /home/akhil/Alphacoders/code/'+filename+';docker rmi '+filename+':'+filename)
            ans = open('code/'+filename+'/answers.txt', "r")
            Verfiy = ans.read()
            if 'done' in Verfiy :
                User = request.user
                p = Profile.objects.get(email=User)
                print(p.id)
                try:
                    solve = Solved.objects.get(user=p.id, ques=pi.qid)
                    messages.success(request, 'Correct solution but you get points only once. try new questions')
                    return render(request, 'view-question.html',context)
                except Exception:
                    e = Solved(user=User,ques=pi.qid)
                    e.save()
                    t = Profile.objects.get(email=User)
                    t.point += int(pi.points)
                    t.save(update_fields=['point'])
                    messages.success(request, 'Correct solution but you get points {}. Keep going'.format(pi.points))
                    return render(request, 'view-question.html',context,)
            else:
                messages.success(request, 'Check your code there is some error')
                return render(request, 'view-question.html',context)
    return render(request, 'view-question.html',context)
