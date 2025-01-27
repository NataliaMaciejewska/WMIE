
import locale
import os

from django.conf import settings
from django.db.models import Q
from django.db.models.functions import Lower
from django.http import FileResponse
from django.shortcuts import render, redirect

from .forms import SubjectsForm, FilesSubjectForm, FilesProjectForm, ProjectsForm
from .models import Subjects, FieldsOfStudy, FilesSubject, FilesProject, Projects
from Users.models import NewUser

locale.setlocale(locale.LC_COLLATE, 'en_US.UTF-8')


# w tym pliku tworzone są funkcje zwracające dane do widoków


def get_subject_by_id(request, id):
    subject = Subjects.objects.get(id=id)
    return render(request, 'subjects_detail.html', {'subject': subject})


def download_file_subject(request, file_name, subject_name, fos_name):
    fos = FieldsOfStudy.objects.filter(name=fos_name).get()
    subject = Subjects.objects.filter(name=subject_name, FieldsOfStudy=fos).get()
    file = FilesSubject.objects.filter(name=file_name, subject=subject).get()
    file_full_path = os.path.join(settings.MEDIA_ROOT, file.file.name)
    print(file_full_path)
    if os.path.exists(file_full_path):
        file.counter = file.counter + 1
        file.save()
        return FileResponse(open(file_full_path, 'rb'), as_attachment=True)
    else:
        pass


def download_file_project(request, file_name, project_name):
    project = Projects.objects.filter(name=project_name).first()
    file = FilesProject.objects.filter(name=file_name, project=project).first()
    print(file.counter)
    file_full_path = os.path.join(settings.MEDIA_ROOT, file.file.name)
    if os.path.exists(file_full_path):
        file.counter = file.counter + 1
        file.save()
        return FileResponse(open(file_full_path, 'rb'), as_attachment=True)
    else:
        pass


def files_by_subject(request, subject, fos):
    project_list = Projects.objects.all()
    fos_list = FieldsOfStudy.objects.all()
    fos = FieldsOfStudy.objects.filter(name=fos).first()
    subject_object = Subjects.objects.filter(Q(name=subject) & Q(FieldsOfStudy=fos)).first()

    files = subject_object.filessubject_set.all().order_by(Lower('name'))
    sorted_list = sorted(files, key=lambda x: locale.strxfrm(str(x.name)))
    # return sorted_list
    return render(request, 'files_subject.html', {'files': sorted_list,
                                                  'fos_list': fos_list,
                                                  'project_list': project_list,
                                                  'fos': fos,
                                                  'subject_name': subject})


def files_by_project(request, project_name):
    project_list = Projects.objects.all()
    fos_list = FieldsOfStudy.objects.all()
    project = Projects.objects.filter(name=project_name).first()

    files = project.filesproject_set.all().order_by(Lower('name'))
    sorted_list = sorted(files, key=lambda x: locale.strxfrm(str(x.name)))
    # return sorted_list
    return render(request, 'files_project.html', {'files': sorted_list,
                                                  'project_list': project_list,
                                                  'fos_list': fos_list,
                                                  'project_name': project_name})


def create_subject(request):
    if request.method == 'POST':
        form = SubjectsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('subjects_list')
    else:
        form = SubjectsForm()
    return render(request, 'create_subject.html', {'form': form})


def create_project(request):
    if request.method == 'POST':
        form = ProjectsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('subjects_list')
    else:
        form = ProjectsForm()
    return render(request, 'create_project.html', {'form': form})


def create_file_subject(request):
    if request.method == 'POST':
        form = FilesSubjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('subjects_list')
    else:
        form = FilesSubjectForm()
    return render(request, 'create_file_subject.html', {'form': form})


def create_file_project(request):
    if request.method == 'POST':
        form = FilesProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('subjects_list')
    else:
        form = FilesProjectForm()
    return render(request, 'create_file_project.html', {'form': form})


def subjects_list(request):
    fos_list = FieldsOfStudy.objects.all()
    project_list = Projects.objects.all()
    return render(request, 'main_dashboard.html', {'fos_list': fos_list,
                                                   'project_list': project_list})


def get_subject_by_fos(request, fos_name, html_name):
    fos_list = FieldsOfStudy.objects.all()
    project_list = Projects.objects.all()

    fos = FieldsOfStudy.objects.filter(name=fos_name).first()

    subjects = Subjects.objects.filter(FieldsOfStudy=fos).values('semester').distinct()

    semesters_list = [item['semester'] for item in subjects]
    result_dict = dict()
    for semester in semesters_list:
        queryset_result = Subjects.objects.filter(Q(semester=semester) & Q(FieldsOfStudy=fos))
        result_dict[semester] = queryset_result

    res = sorted(result_dict.items())

    return render(request, html_name, {'result_dict': dict(res),
                                       'fos_list': fos_list,
                                       'current_fos': fos,
                                       'project_list': project_list})


# dane do wykresow
def diagram_view(request):
    AllFOS = FieldsOfStudy.objects.all()

    output = dict()

    fos_labels = []
    fos_data = []

    for fos in AllFOS:
        counter_fos = 0
        subjects = Subjects.objects.filter(FieldsOfStudy=fos)
        labels = []
        data = []
        for subject in subjects:
            counter_subject = 0
            files = subject.filessubject_set.all()
            for file in files:
                counter_fos = counter_fos + file.counter
                counter_subject = counter_subject + file.counter
            labels.append(subject.name)
            data.append(counter_subject)
            output[fos.name.replace(" ", "_") + "_label"] = labels
            output[fos.name.replace(" ", "_") + "_data"] = data
        fos_data.append(counter_fos)
        fos_labels.append(fos.name)

    fos = FieldsOfStudy._meta.object_name
    output[fos.replace(" ", "_") + '_label'] = fos_labels
    output[fos.replace(" ", "_") + '_data'] = fos_data

    projects = Projects.objects.all()

    labels = []
    data = []

    for project in projects:

        counter_project = 0
        files = project.filesproject_set.all()
        for file in files:
            counter_project = counter_project + file.counter
        labels.append(project.name)
        data.append(counter_project)

    pro = Projects._meta.object_name
    output[pro.replace(" ", "_") + '_label'] = labels
    output[pro.replace(" ", "_") + '_data'] = data

    SexLabels = []
    SexData = []

    VoiLabels = []
    VoiData = []

    sexQuery = NewUser.objects.raw('select id, sex, count(*) as counter_fos from Users_newuser group by sex')
    for i in sexQuery:
        SexLabels.append(i.sex)
        SexData.append(i.counter_fos)

    voiQuery = NewUser.objects.raw(
        'select id, voivodeship, count(*) as counter_fos from Users_newuser group by voivodeship')
    for i in voiQuery:
        VoiLabels.append(i.voivodeship)
        VoiData.append(i.counter_fos)

    output['SexLabels'] = SexLabels
    output['SexData'] = SexData

    output['VoiLabels'] = VoiLabels
    output['VoiData'] = VoiData

    print(output)

    return render(request, 'diagrams.html', output)


def getDashboard(request, fos_name):
    return get_subject_by_fos(request, fos_name, 'subjects.html')


def getDashboardProject(request, project_name):
    return files_by_project(request, project_name)


def admin_panel(request):
    return render(request, 'admin.site.urls')
