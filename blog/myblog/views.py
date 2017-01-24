from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import BlogPagePostForm

# Create your views here.
@login_required
def post_new(request):
    if request.method == "POST":
        form = BlogPagePostForm(request.POST)

        # form validation
        if form.is_valid():
            # commit false to prevent save form, because author isnt filled in by the user
            post = form.save(commit=False)
            post.author = request.user
            # function to post new blogpost instantly if uncommented.
            # post.published_date = timezone.now()
            post.save()

            # redirect user to post detail page using its primary key
            # return redirect('post_detail', pk=post.pk)

    else:
        form = BlogPagePostForm()

    return render(request, 'form/post_edit.html', {'form': form})
