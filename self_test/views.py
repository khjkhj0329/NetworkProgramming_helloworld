from django.shortcuts import render

def hyunwook(request):
    context1 = {
        'name' : '최현욱',
        'img_src':'https://t1.daumcdn.net/liveboard/whynotmedia/049c0134a8724ede8ba2061d708c2d72.JPG',
    }
    return render(request, "self_test/member.html", context=context1)

def secopahn(request):
    context2 = {
        'name': '안효섭',
        'img_src':'https://img.marieclairekorea.com/2022/03/mck_621eda8d55ba3-562x570.jpeg',
    }
    return render(request, "self_test/member.html", context=context2)


