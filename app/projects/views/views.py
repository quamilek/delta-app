from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

import pandas as pd
from projects.forms import ImportProjectForm
from projects.models import ProjectElement, Project
from django.contrib import messages


@login_required
def import_project(request):
    if request.method == 'POST':
        form = ImportProjectForm(request.POST, request.FILES)

        if form.is_valid():
            project_file = request.FILES["projectFile"]
            fs = FileSystemStorage()
            # save file in storage
            filename = fs.save(project_file.name, project_file)
        
            file_data = pd.read_excel(project_file, skiprows=1)

            project_name = get_project_name_form_file(file_data)
            

            count = Project.objects.filter(name=project_name).count()
            if count > 0:
                messages.add_message(request, messages.ERROR, "Projekt o takiej nazwie istnieje\n zmień nazwę projektu i dodaj ponownie")
                return render(request, 'upload.html', {'form': form})


            form.instance.name = project_name
            form.save()

            project_obj = form.instance
            create_project_elements_from_file_data(file_data, project_obj)

            return redirect('project', project_obj.id)  # Redirect to success page
        else:
            # Handle form errors, e.g., display them in the template
            return render(request, 'upload.html', {'form': form})
    else:

        # messages.add_message(request, messages.SUCCESS, "Hello world.")
        # messages.add_message(request, messages.ERROR, "Hello world.")
        form = ImportProjectForm()
    return render(request, 'upload.html', {'form': form})


def get_project_name_form_file(file_data): 
    return file_data.head()['Project Name'][1]

def create_project_elements_from_file_data(file_data, project_obj):
    # bez ostatniego wiersza bo tam jest sumowanie
    for row_dict in file_data[:-1].to_dict(orient="records"):
        row_lowercase = {transform_table_column_name(k.lower()): v for k, v in row_dict.items()}
        
    
        project_element = ProjectElement(**row_lowercase)
        project_element.project = project_obj
        project_element.save()

def transform_table_column_name(value):
    if value in REPLACE_COLUMN_NAMES.keys():
        return REPLACE_COLUMN_NAMES[value]
    else:
        return value
    
REPLACE_COLUMN_NAMES = {
    'ref.' : 'ref',
    'tq/pr' : 'tq_pr',
    'project name': 'project_name',
    'prod.' : 'prod',
    'ppc side' : 'ppc_side',
    'total lm' : 'total_lm',
    'total m2' : 'total_m2',
    'height.1' : 'height_1',
    'width.1' : 'width_1',
    'qty.1' : 'qty_1',
    'toal lm' : 'total_lm_1',
    'total m2.1' : 'total_m2_1',
    'priority 1' : 'priority_1',
    'phase ': 'phase',
    'elev.' : 'elev'
}