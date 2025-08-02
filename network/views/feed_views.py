from django.views.generic import TemplateView

class FeedView(TemplateView):
    template_name = "network/feed.html"