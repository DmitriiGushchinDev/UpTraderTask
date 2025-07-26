from django.db import models
from django.urls import reverse, NoReverseMatch
from django.http import Http404


class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=200, blank=True)
    menu_name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')


    def get_url(self):
        parts = [self.url]
        parent = self.parent
        while parent:
            parts.insert(0, parent.url or parent.title.lower())
            parent = parent.parent
        return '/' + '/'.join(part.strip('/') for part in parts) + '/'  if self.url else '/'   

    def __str__(self):
        return self.title
    

