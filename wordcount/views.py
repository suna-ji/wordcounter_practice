from django.shortcuts import render
from django.http import HttpResponse
import json #파이썬은 기본적으로 JSON표준 라이브러리 json을 제공하고 있는데 import json로 사용가능하다

# Create your views here.

def home(request):
    return render(request, 'home.html')
    
def about(request):
    return render(request, 'about.html')

def result(request):
    # ajax통신->새로고침 없이 버튼클릭감지&$.ajax()를 통해서 서버와 통신 시작
    # url pattern분석 후 view이동
    # model DB작업
    # Json형식으로 Data 전달-> 서버측에서 전송한 response데이터(json)을 동적으로 html에 반영
    # 즉 jQuery를 활용하여 서버로부터 받은 Data를 동적으로 html에 추가
    #json은 JavaScript Object Notation의 약자로서 JavaScript문법에 영향을 받아 개발된 Lightweight한 
    #데이터 표현 방식이다. JSON은 데이터를 교환하는 한 포맷으로서 그 단순함과 유연함 때문에 널리 사용되고 있다
    # 특히 웹 브라우저와 웹서버 사이에 데이터를 교환하는데 많이 사용되고 있다.
    # 가장 많이 사용되는 포맷을 Key-Value pair의 컬렉션이다. // key : value
    if request.is_ajax():
        fulltext = request.GET['fulltext']
        word_list = fulltext.split()
        word_dictionary = {}
        for word in word_list:
            if word in word_dictionary:
                word_dictionary[word]+=1
            else:
                word_dictionary[word] = 1  
        data = { 'fulltext': fulltext, 'total': len(word_list), 'dictionary': list(word_dictionary.items())}
        #JSON 인코딩
        # python object(Dictonay, List, Tuple) --(변경)-> JSON 문자열
        # 우선 json라이브러리 import하고 json.dumps()메소드를 써서 python Object를 문자열로 변환하면 된다   
        return  HttpResponse(json.dumps(data), "application/json")        
    return render(request, 'result.html', {'fulltext':fulltext, 'total':len(word_list), 'dictionary':word_dictionary.items()})  

    