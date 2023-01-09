from django.shortcuts import render
from . models import Post
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView
from django.http import Http404
# Create your views here.
def post_list(request):
    all_post=Post.objects.all().order_by('id')
    paginator=Paginator(all_post,3)
    page_number =request.GET.get('page')
    page_obj =paginator.get_page(page_number)
    return render(request,'blog/home.html',{'page_obj':page_obj})


class PostListView(ListView):
    model =Post
    template_name='blog/home.html'
    ordering=['id']
    paginate_by=3
    paginate_orphans=1
    def get_context_data(self, **kwargs):
            context=super().get_context_data(**kwargs)
            context['view']='Class Based'
            return context
    # def get_context_data(self, **kwargs):
    #     try:
    #         context=super().get_context_data(**kwargs)
    #         context['view']='Class Based'
    #         return context
    #     except Http404:
    #         self.kwargs['page']=1
    #         context=super().get_context_data(**kwargs)
            # context['view']='Class Based'
            # return context
    def paginate_queryset(self, queryset, page_size):
            try:
                return super().paginate_queryset(queryset, page_size)
            
            except Http404:
                self.kwargs['page']=1
                return super().paginate_queryset(queryset, page_size)
                
class PostDetailView(DetailView):
    model=Post
    template_name='blog/post.html'