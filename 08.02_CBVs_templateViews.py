# Function Based Views:
def index(request):
  return render(request,'index.html')

# Class Based Template Views:
class IndexView(TemplateView):
  template_name = 'index.html'