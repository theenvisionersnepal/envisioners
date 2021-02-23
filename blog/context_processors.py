from .models import Category, BlogPost


def menu_categories(request):
    categories = Category.objects.all()
    return {'menu_categories': categories}
