from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    text = request.GET['fulltext']
    
    text_split = text.split(' ')

    word_dic = {}

    for word in text_split:
        if word in word_dic.keys():
            word_dic[word] += 1
        else:
            word_dic[word] = 1


    return render(request, 'count.html', {
                                            'length' : len(text_split),
                                            'full' : text_split,
                                            'text' : text,
                                            'dic' : word_dic.items(),
                                            })