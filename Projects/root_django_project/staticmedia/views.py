from django.shortcuts import render
# importing FileSystemStorage for storing files
from django.core.files.storage import FileSystemStorage


# Create your views here.

def render_static(request):
    return render(request, 'static.html')


# creating view for media 
def manage_media(request):
    # applying logics for post method
    if request.method == 'POST':
        print(" post data-->", request.POST)
        print("uploaded files is-->", request.FILES)
        # we can use logics on validating and storing the files

        # assigning the files from html templates
        file_obj = request.FILES['myfile']

        # fs object creation
        print("my file name is --->", file_obj.name)
        fs = FileSystemStorage()

        # overriding the file name
        # __file_name = 'image/my/ok.jpg'

        # storing with save method passing attribute.name
        # filename = fs.save(__file_name, file_obj)

        filename = fs.save(file_obj.name, file_obj)

        # url = settingss media url + fileref
        # django automate file url too
        file_url = fs.url(filename)
        print("after saving or uploaded filename is -->", filename)
        print(" My file url is --->", file_url)



    return render(request, 'media.html')

    # focus and reserach on external validations of uploading images files only
    # users may upload unwanted and miscellaneous files instead of required images