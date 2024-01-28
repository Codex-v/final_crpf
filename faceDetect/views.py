from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from .utils import Util
from .serizailer import imageform
from django.conf import settings as s
from django.views.decorators.csrf import csrf_protect
import json


@csrf_protect
def facescan(request):
    result = [0]
    if request.method == "POST":
            form = imageform(request.POST,request.FILES)
            data =request.FILES['image']
            image_name = Util.handle_uploaded_file(request.FILES['image'])
            total_number_files = Util.count_items_in_folder(f'{s.BASE_DIR}\\facedetect\\media')
            print(total_number_files)
            media_directory = f'{s.BASE_DIR}\\facedetect\\media'
            result = Util.compare_faces_with_uploaded_image(image_name)
            print(result)
            if result == "Result Not Found":
                return JsonResponse({"message":"match not found!"},status=404)

            if result[0] == True:
                print(result[1],"this is result")
                # binary_data = Util.imagetoBinary(f'{s.BASE_DIR}\\facedetect\\media\\{result[0]}')
                # response = HttpResponse(f'\\facedetect\\media\\{result[0]}', content_type='image/jpeg')
                # response['Content-Disposition'] = 'attachment; filename="image.jpg"'
                # print(response)
                json_data = ""
                json_name = str(result[1]).replace(".jpg",".json").replace(".png",".json")
                print("json_name",json_name)
                with open(f'{s.BASE_DIR}\\facedetect\\media\\{json_name}',"r") as file:
                    json_data = json.load(file)
                return JsonResponse({'img':f'\\media\\{result[1]}','data':json_data},status=200)
            else:
                return JsonResponse({"message":"match not found!"},status=404)
    else:
            params = {"img": f'{s.BASE_DIR}',"all_imgs_path":f'm'}
            return render(request, 'find-criminal.html',params)

@api_view(["POST"])
def getdata(request):
    if request:
        image = request.FILES['image']
        images_name = Util.handle_media_file(image,"file")
        name = request.POST.get('name')
        bloodgroup = request.POST.get('bloodGroup')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        criminalrecord = request.POST.get('criminalrecord')

        data = {"name":name,"bloodgroup":bloodgroup,"gender":gender,"age":age,"criminalrecord":criminalrecord}
        final_name = str(images_name).replace(".jpg","").replace(".png","")
        finaldata = json.dumps(data)
        with open(f"{s.BASE_DIR}\\facedetect\\media\\{final_name}.json","w+") as file:
                file.writelines(finaldata)
                file.close() 
        return HttpResponse("Criminal record set")
    else:
        return HttpResponse("record not set")
            
def addcriminal(request):
    if request.method == "POST":
        image = request.FILES['image']
        images_name = Util.handle_media_file(image,"file")
        name = request.POST.get('name')
        bloodgroup = request.POST.get('bloodgroup')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        criminalrecord = request.POST.get('criminalrecord')
        data = {"name":name,"bloodgroup":bloodgroup,"gender":gender,"age":age,"criminalrecord":criminalrecord}
        final_name = str(images_name).replace(".jpg","").replace(".png","")
        finaldata = json.dumps(data)
        with open(f"{s.BASE_DIR}\\facedetect\\media\\{final_name}.json","w+") as file:
                file.writelines(finaldata)
                file.close() 
        return redirect("dashboard")
    else:
        return render(request, 'add-criminal.html')

