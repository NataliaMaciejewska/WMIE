import locale
import logging
import os
from collections import Counter
from lib2to3.fixes.fix_input import context

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.db.models import Sum, Count
from django.db.models.functions import Lower
from django.forms import modelformset_factory
from django.http import FileResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .forms import FilesProjectForm, ProjectsForm, FilesFosForm, QuizForm, QuestionForm
from .models import FieldsOfStudy, FilesProject, Projects, Application, VisitCount, FilesFieldsOfStudy, Quiz, Question, \
    Answer
from users.models import NewUser

logger = logging.getLogger(__name__)


def view_file_project(request, file_name, project_name):
    project = Projects.objects.filter(name=project_name).first()
    if not project:
        raise Http404("Project not found")

    file = FilesProject.objects.filter(name=file_name, project=project).first()
    if not file:
        raise Http404("File not found")

    file_full_path = os.path.join(settings.MEDIA_ROOT, file.file.name)
    if os.path.exists(file_full_path):
        return FileResponse(open(file_full_path, 'rb'))  # bez as_attachment=True — wyświetla plik
    else:
        raise Http404("File does not exist")



def view_file_fos(request, file_name, fos_name):
    fos = FieldsOfStudy.objects.filter(name=fos_name).first()
    if not fos:
        raise Http404("Field of Study not found")

    file = FilesFieldsOfStudy.objects.filter(name=file_name, fos=fos).first()
    if not file:
        raise Http404("File not found")

    file_full_path = os.path.join(settings.MEDIA_ROOT, file.file.name)
    if os.path.exists(file_full_path):
        return FileResponse(open(file_full_path, 'rb'))
    else:
        raise Http404("File does not exist")



def files_by_project(request, id):
    project_list = Projects.objects.all()
    fos_list = FieldsOfStudy.objects.all()
    project = Projects.objects.filter(id=id).first()
    logger.info(id)
    files = Projects.objects.filter(id=id).first().filesproject_set.all().order_by(Lower('name'))
    sorted_list = sorted(files, key=lambda x: locale.strxfrm(str(x.name)))
    return render(request, 'project_dashboard.html', {'files': sorted_list,
                                                      'project_list': project_list,
                                                      'fos_list': fos_list,
                                                      'project_name': project.name

                                                      })


def files_by_fos(request, id):
    project_list = Projects.objects.all()
    fos_list = FieldsOfStudy.objects.all()
    fos = FieldsOfStudy.objects.filter(id=id).first()
    logger.info(id)
    logger.info(fos)

    files = fos.filesfieldsofstudy_set.all().order_by(Lower('name'))

    logger.info(files)
    sorted_list = sorted(files, key=lambda x: locale.strxfrm(str(x.name)))

    return render(request, 'fos_dashboard.html', {'files': sorted_list,
                                                  'project_list': project_list,
                                                  'fos_list': fos_list,
                                                  'fos': fos,
                                                  })


def create_project(request):
    if request.method == 'POST':
        form = ProjectsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main_dashboard')
    else:
        form = ProjectsForm()
    return render(request, 'create_project.html', {'form': form})


def create_file_fos(request):
    if request.method == 'POST':
        form = FilesFosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main_dashboard')

    else:
        form = FilesFosForm()
    return render(request, 'create_file_fos.html', {'form': form})


def create_file_project(request):
    if request.method == 'POST':
        form = FilesProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main_dashboard')
    else:
        form = FilesProjectForm()
    return render(request, 'create_file_project.html', {'form': form})


def main_dashboard(request):

    fos_list = FieldsOfStudy.objects.all()

    logging.info(fos_list)

    project_list = Projects.objects.all()

    app_name = Application.objects.first().name

    app_description = Application.objects.first().description
    app_background_path = Application.objects.first().background_path

    return render(request, 'main_dashboard.html',
                  {'fos_list': fos_list, 'project_list': project_list, "app_name": app_name,
                   "app_description": app_description,'background_path': app_background_path } )


def diagram_view(request):
    output = {}

    visit_counts = VisitCount.objects.values('fieldOfStudy__name').annotate(
        total=Sum('counter')
    )

    fos_labels = []
    fos_data = []
    for item in visit_counts:
        if item['fieldOfStudy__name'] is None:
            pass
        else:
            fos_labels.append(item['fieldOfStudy__name'])
            fos_data.append(item['total'])

    output['FieldsOfStudy_label'] = fos_labels
    output['FieldsOfStudy_data'] = fos_data

    sex_counts = VisitCount.objects.values('sex').annotate(count=Sum('counter'))
    output['SexLabels'] = [item['sex'] for item in sex_counts if item['sex']]
    output['SexData'] = [item['count'] for item in sex_counts if item['sex']]

    voi_counts = VisitCount.objects.values('voivodeship').annotate(count=Sum('counter'))
    output['VoiLabels'] = [item['voivodeship'] for item in voi_counts if item['voivodeship']]
    output['VoiData'] = [item['count'] for item in voi_counts if item['voivodeship']]

    logger.info(f"Final output: {output}")

    return render(request, 'diagrams.html', output)


def get_project_dashboard(request, id):
    return files_by_project(request, id)


def get_fos_dashboard(request, id):
    user = request.user

    voivodeship = getattr(user, 'voivodeship', None)
    sex = getattr(user, 'sex', None)

    getOrCreateVisitCount(voivodeship, sex, field_of_study_id=id)

    # Pobierz kierunek (fields of study)
    fos = FieldsOfStudy.objects.filter(id=id).first()

    # Pobierz pliki przypisane do tego kierunku (zgodnie z tym co robi get_files_by_fos)
    files_fos = fos.filesfieldsofstudy_set.all()

    logging.info(files_fos)

    # Pobierz quizy dla tego kierunku
    quiz_list = Quiz.objects.filter(fos=fos)
    all_fos = FieldsOfStudy.objects.all()

    context = {
        'files_fos': files_fos,
        'fos': fos,
        'quiz_list': quiz_list,
        'fields_of_study': all_fos,
    }

    # Renderuj ten sam szablon, który używasz w get_files_by_fos,
    # czyli np. 'some_template.html' — podmień na Twój faktyczny
    return render(request, 'fos_dashboard.html', context)

def admin_panel(request):
    return render(request, 'admin.site.urls')


def getOrCreateVisitCount(voivodeship, sex, field_of_study_id=None):
    visit_count, created = VisitCount.objects.get_or_create(fieldOfStudy_id=field_of_study_id, voivodeship=voivodeship, sex=sex)
    visit_count.counter += 1
    visit_count.save()

############### quizy #################

def create_quiz(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.created_by = request.user
            quiz.save()
            return redirect('add_question', quiz_id=quiz.id)
    else:
        form = QuizForm()
    return render(request, 'create_quiz.html', {'form': form})

def add_question(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)

    if request.method == 'POST':
        i = 0
        while f'question_{i}' in request.POST:
            question_text = request.POST.get(f'question_{i}')
            correct_index = int(request.POST.get(f'correct_{i}', 1)) - 1  # 0-based

            question = Question.objects.create(quiz=quiz, text=question_text)

            for j in range(4):
                answer_text = request.POST.get(f'answer_{i}_{j}', '').strip()
                if answer_text:
                    Answer.objects.create(
                        question=question,
                        text=answer_text,
                        is_correct=(j == correct_index)
                    )
            i += 1

        messages.success(request, 'Pytania zostały zapisane!')

    return render(request, 'add_question.html', {'quiz': quiz})
def quizzes_by_fos(request, fos_id):
    quizzes = Quiz.objects.filter(fos_id=fos_id)
    return render(request, 'quizzes_by_fos.html', {
        'quizzes': quizzes,
        'fos_id': fos_id,
    })

from django.shortcuts import get_object_or_404, render
from .models import Quiz, Question, Answer

def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    questions = quiz.question_set.prefetch_related('answers')

    if request.method == 'POST':
        submitted_answers = {
            int(k.split('_')[1]): int(v)
            for k, v in request.POST.items()
            if k.startswith('question_')
        }

        correct_count = 0

        for question in questions:
            selected_id = submitted_answers.get(question.id)
            correct_answer = question.answers.filter(is_correct=True).first()
            question.selected_id = selected_id
            question.correct_id = correct_answer.id if correct_answer else None
            if selected_id == question.correct_id:
                correct_count += 1

        return render(request, 'quiz_detail.html', {
            'quiz': quiz,
            'questions': questions,
            'submitted': True,
            'correct_count': correct_count,
            'total_count': questions.count()
        })

    return render(request, 'quiz_detail.html', {
        'quiz': quiz,
        'questions': questions,
        'submitted': False,
    })
