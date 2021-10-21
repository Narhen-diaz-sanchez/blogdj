from django.contrib.sitemaps import Sitemap
from datetime import datetime
from django.urls import reverse_lazy
from applications.entradas.models import Entry

class EntrySitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8
    protocol = 'htpps'
    
    def items(self):
        return Entry.objects.filter(public=True)
    
    def lastmod(self, obj):
        return obj.created
    
    
class Sitemap(Sitemap):
    protocol = 'https'
    
    def __init__(self, names):
        self.names = names
        
    def items(self):
        return self.names
    
    def changefreq(self, obj):
        return 'weekly'
    
    def lastmod(self, obj):
        return datetime.now()  
    
    def location(self, obj):
        return reverse_lazy(obj)
    