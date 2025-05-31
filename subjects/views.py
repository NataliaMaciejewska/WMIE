import locale
import logging
import os
from collections import Counter

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models import Sum, Count
from django.db.models.functions import Lower
from django.http import FileResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import FilesProjectForm, ProjectsForm, FilesFosForm
from .models import FieldsOfStudy, FilesProject, Projects, Application, VisitCount, FilesFieldsOfStudy
from users.models import NewUser

logger = logging.getLogger(__name__)


def download_file_project(request, file_name, project_name):
    project = Projects.objects.filter(name=project_name).first()
    file = FilesProject.objects.filter(name=file_name, project=project).first()
    file_full_path = os.path.join(settings.MEDIA_ROOT, file.file.name)
    if os.path.exists(file_full_path):
        file.save()
        return FileResponse(open(file_full_path, 'rb'), as_attachment=True)
    else:
        pass


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


def get_files_by_fos(request, fos_name, html_name):
    fos = FieldsOfStudy.objects.filter(name=fos_name).first()

    files_fos = FieldsOfStudy.objects.filter(FieldsOfStudy=fos).first().filesfieldsofstudy_set.all()

    return render(request, html_name, {'files_fos': files_fos, 'current_fos': fos})


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
    return files_by_fos(request, id)


def admin_panel(request):
    return render(request, 'admin.site.urls')


def getOrCreateVisitCount(voivodeship, sex, field_of_study_id=None):
    visit_count, created = VisitCount.objects.get_or_create(fieldOfStudy_id=field_of_study_id, voivodeship=voivodeship, sex=sex)
    visit_count.counter += 1
    visit_count.save()
