from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import EmptyPage, InvalidPage, PageNotAnInteger, Paginator


def paginate(objects_list, request, count_obj):
    page_number = request.GET.get('page')
    if page_number is None:
        page_number = 1

    paginator = Paginator(objects_list, count_obj)
    if paginator.num_pages == 0:
        return None, None

    try:
        page = paginator.page(page_number)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    except InvalidPage:
        page = paginator.page(1)

    return page.object_list, page


questions = {
    i: {'id': i, 'title': f'# {i}', 'tags': ["MGTU", "IU"]}
    for i in range(1, 20)
}

question_list = []
for i in range(1, 20):
    question_list.append(questions[i])

answers = {
    i: {'id': i}
    for i in range(3)
}


def index(request):
    question_page, page = paginate(question_list, request, 3)
    return render(request, 'index.html', {
        'hot': False,
        'questions': question_page,
        'page': page,
    })


def login(request):
    return render(request, 'login.html', {})


def signup(request):
    return render(request, 'register.html', {})


# @login_required
def ask(request):
    return render(request, 'ask.html', {})


def settings(request):
    return render(request, 'settings.html', {})


def hot(request):
    question_page, page = paginate(question_list, request, 3)
    return render(request, 'index.html', {
        'hot': True,
        'questions': question_page,
        'page': page,
    })


def question(request, qid):
    quest = questions.get(qid)
    answers_page, page = paginate(question_list, request, 3)
    return render(request, 'question.html', {
        'question': quest,
        'answers':answers_page,
        'page': page,
    })


def tag(request, tag_name):
    question_page, page = paginate(question_list, request, 3)
    return render(request, 'tag.html', {
        'tag': tag_name,
        'questions': question_page,
        'page': page,
    })
