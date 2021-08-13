from django import forms

from forum.models import Question, Comment


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']
        labels = {
            'subject': '제목',
            'content': '내용',
        }



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }