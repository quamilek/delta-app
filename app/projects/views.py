from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
import pandas as pd
from projects.forms import ImportProjectForm


@login_required
def import_project(request):
    # if request.method == "POST" and request.FILES["image_file"]:
    #     image_file = request.FILES["image_file"]
    #     fs = FileSystemStorage()
    #     filename = fs.save(image_file.name, image_file)
        
    #     data = pd.read_excel(image_file, skiprows=1)
    #     image_url = fs.url(filename)
        
    #     import pdb; pdb.pdb.set_trace()


    #     teststring = data.head(1)

    #     print(image_url)
    #     return render(request, "upload.html", {
    #         "image_url": image_url,
    #         "teststring": teststring,
    #     })
    if request.method == 'POST':
        form = ImportProjectForm(request.POST, request.FILES)  # Access uploaded file

        if form.is_valid():
            project_file = request.FILES["projectFile"]
            fs = FileSystemStorage()
            filename = fs.save(project_file.name, project_file)
        
            data = pd.read_excel(project_file, skiprows=1)
    #     image_url = fs.url(filename)
            
            zapisywanie projeckt name 
            form.instance.name = "dupa"
            import ipdb;ipdb.set_trace()

            project_name = data.head()['Project Name'][1]

            form.sa
            
            client_name = form.cleaned_data['client_name']
            file_upload = form.cleaned_data['file_upload']  # Handle uploaded file if present


            
            # Process form data here
            # Save to database, send email, perform actions, etc.

            return redirect('success_url')  # Redirect to success page
        else:
            # Handle form errors, e.g., display them in the template
            return render(request, 'upload.html', {'form': form})
    else:
        form = ImportProjectForm()
    return render(request, 'upload.html', {'form': form})
