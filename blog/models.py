from django.db import models

# Create your models here.
from wagtail.models import Page
from wagtail.fields import RichTextField

class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + ["intro"]