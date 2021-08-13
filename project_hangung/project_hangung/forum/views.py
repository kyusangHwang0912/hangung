from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from .models import Question, Answer, Comment, Image
from django.utils import timezone
from .forms import QuestionForm, AnswerForm, CommentForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q, Count

def index(request):
    """
    forum 목록 출력
    """
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    so = request.GET.get('so', 'recent')  # 정렬기준
    gung = request.GET.get('gung', 'all') # gung category


    # 카테고리
    if gung == 'all':
        if so == 'recommend':
            question_list = Question.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
        elif so == 'popular':
            question_list = Question.objects.annotate(num_answer=Count('answer')).order_by('-num_answer', '-create_date')
        else:  # recent
            question_list = Question.objects.order_by('-create_date')
    elif gung == 'gyeongbokgung':
        if so == 'recommend':
            question_list = Question.objects.filter(gung='경복궁').annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
        elif so == 'popular':
            question_list = Question.objects.filter(gung='경복궁').annotate(num_answer=Count('answer')).order_by('-num_answer', '-create_date')
        else:  # recent
            question_list = Question.objects.filter(gung='경복궁').order_by('-create_date')
    elif gung == 'changdukgung':
        if so == 'recommend':
            question_list = Question.objects.filter(gung='창덕궁').annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
        elif so == 'popular':
            question_list = Question.objects.filter(gung='창덕궁').annotate(num_answer=Count('answer')).order_by('-num_answer', '-create_date')
        else:  # recent
            question_list = Question.objects.filter(gung='창덕궁').order_by('-create_date')
    elif gung == 'changgyunggung':
        if so == 'recommend':
            question_list = Question.objects.filter(gung='창경궁').annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
        elif so == 'popular':
            question_list = Question.objects.filter(gung='창경궁').annotate(num_answer=Count('answer')).order_by('-num_answer', '-create_date')
        else:  # recent
            question_list = Question.objects.filter(gung='창경궁').order_by('-create_date')
    else:
        if so == 'recommend':
            question_list = Question.objects.filter(gung='덕수궁').annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
        elif so == 'popular':
            question_list = Question.objects.filter(gung='덕수궁').annotate(num_answer=Count('answer')).order_by('-num_answer','-create_date')
        else:  # recent
            question_list = Question.objects.filter(gung='덕수궁').order_by('-create_date')
    # 조회
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목검색
            Q(content__icontains=kw) |  # 내용검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이검색
        ).distinct()

    # 페이징처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj, 'page': page, 'kw': kw, 'so':so, 'gung':gung}
    return render(request, 'question_list.html', context)


def detail(request, question_id):
    """
    forum 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'question_detail.html', context)


@login_required(login_url='common:login')
def question_create(request):
    """
    forum 질문등록
    """
    gung = request.POST.get('gung','경복궁')

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.create_date = timezone.now()
            question.gung = gung
            question.save()
            for data in request.FILES.getlist('multiphoto'):
                # Photo 객체를 하나 생성한다.
                image = Image()
                # 외래키로 현재 생성한 question의 기본키를 참조한다.
                image.question = question
                # multiphoto로부터 가져온 이미지 파일 하나를 저장한다.
                image.photo = data
                # 데이터베이스에 저장
                image.save()
        return redirect('forum:index')
    else:
        form = QuestionForm()
    context = {'form': form,}
    return render(request, 'question_form.html', context)

@login_required(login_url='common:login')
def question_modify(request, question_id):
    """
    forum 질문수정
    """

    gung = request.POST.get('gung', '경복궁')

    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('forum:detail', question_id=question.id)

    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.modify_date = timezone.now()  # 수정일시 저장
            question.gung = gung
            question.save()
            question.image_set.all().delete()
            for data in request.FILES.getlist('multiphoto'):
                # Photo 객체를 하나 생성한다.
                image = Image()
                # 외래키로 현재 생성한 question의 기본키를 참조한다.
                image.question = question
                # multiphoto로부터 가져온 이미지 파일 하나를 저장한다.
                image.photo = data
                # 데이터베이스에 저장
                image.save()
            return redirect('forum:detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'question_form.html', context)


@login_required(login_url='common:login')
def question_delete(request, question_id):
    """
    forum 질문삭제
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('forum:detail', question_id=question.id)
    question.delete()
    return redirect('forum:index')


@login_required(login_url='common:login')
def answer_modify(request, answer_id):
    """
    forum 답변수정
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('forum:detail', question_id=answer.question.id)

    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('{}#answer_{}'.format(
                resolve_url('forum:detail', question_id=answer.question_id), answer.id))
    else:
        form = AnswerForm(instance=answer)
    context = {'answer': answer, 'form': form}
    return render(request, 'answer_form.html', context)


@login_required(login_url='common:login')
def answer_delete(request, answer_id):
    """
    forum 답변삭제
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '삭제권한이 없습니다')
    else:
        answer.delete()
    return redirect('forum:detail', question_id=answer.question.id)

@login_required(login_url='common:login')
def comment_create_question(request, question_id):
    """
    forum 질문댓글등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.question = question
            comment.save()
            return redirect('forum:detail', question_id=question.id)
    else:
        form = CommentForm()
    context = {'form': form}
    return render(request, 'comment_form.html', context)

@login_required(login_url='common:login')
def comment_modify_question(request, comment_id):
    """
    forum 질문댓글수정
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글수정권한이 없습니다')
        return redirect('forum:detail', question_id=comment.question.id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('forum:detail', question_id=comment.question.id)
    else:
        form = CommentForm(instance=comment)
    context = {'form': form}
    return render(request, 'comment_form.html', context)

@login_required(login_url='common:login')
def comment_delete_question(request, comment_id):
    """
    forum 질문댓글삭제
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글삭제권한이 없습니다')
        return redirect('forum:detail', question_id=comment.question_id)
    else:
        comment.delete()
    return redirect('forum:detail', question_id=comment.question_id)


@login_required(login_url='common:login')
def vote_question(request, question_id):
    """
    forum 질문추천등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        question.voter.add(request.user)
    return redirect('forum:detail', question_id=question.id)

