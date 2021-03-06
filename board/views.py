from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render

from board.forms import NewTopicForm
from board.models import Boardx, Post


def home(request):
    """This is a view / function to output helloworld"""
    boards = Boardx.objects.all()
    return render(request, 'home.html', {'boards': boards})


def board_topics(request, id):
    board = get_object_or_404(Boardx, pk=id)

    return render(request, 'topics.html', {'board': board})


def new_topic(request, id):
    board = get_object_or_404(Boardx, pk=id)
    user = User.objects.first()  # TODO: get the currently logged in user
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=user
            )
            return redirect('board_topics', id=board.id)  # TODO: redirect to the created topic page
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', {'board': board, 'form': form})
