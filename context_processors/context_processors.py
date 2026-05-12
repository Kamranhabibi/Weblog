from weblog.models import Article , Category


def context_processors(request):

    recent_articles = Article.objects.order_by('-create')

    categories = Category.objects.order_by('-create')

    return {'recent_articles':recent_articles , 'categories':categories}



