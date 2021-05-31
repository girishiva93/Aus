from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.template.loader import render_to_string
from .meta_gen import meta_keywords


def indexblog(request):
    """
            Display Blog  page

            **Context**

            ``indexblog``
                An instance of :model:`indexblog.Course`

            **Templates**
            :template:`pages/blog.html`
        """
    blogs = Blog.objects.order_by('-list_date').filter(is_published=True)
    context = {
        'blogs': blogs
    }
    return render(request, 'pages/blog.html', context)


def blog(request, blog_id):
    """
        Display Blog detail page

        **Context**

        ``blog``
            An instance of :model:`Blog.blog`

        **Templates**
        :template:`pages/bloginside.html`
    """
    blogdetails = get_object_or_404(Blog, pk=blog_id)
    blogs = Blog.objects.all()[:3]
    context = {
        'blogdetails': blogdetails,
        'blogs': blogs
    }
    return render(request, 'pages/bloginside.html', context)


this_template = "apptemplate.html"


def tabs(request):
    return render(request, {'title': "Blog", 'keys': meta_keywords(render_to_string(this_template))})
