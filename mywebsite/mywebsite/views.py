from django.shortcuts import render

def index(request):
    context = {
        'judul':'Kelas TI C22',
        'subjudul':'Selamat Datang Di TI C22',
        'banner':'img/banner_home.png'
    }
    return render(request,'index.html',context)