from datetime import datetime

def blog_name(request):
    return {'blog_name': 'Inspire Bloom'}

def current_year(request):
    return {'current_year': datetime.now().year}