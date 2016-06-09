from django.db import models
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField, RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailsearch.index import SearchField

from project_tier.blocks import SectionBlock


class StandardIndexPage(Page):
    introductory_headline = models.TextField()

    search_fields = Page.search_fields + [
        SearchField('introductory_headline')
    ]

    content_panels = Page.content_panels + [
        FieldPanel('introductory_headline', classname='full')
    ]

    subpage_types = ['StandardPage']


class StandardPage(Page):
    introductory_headline = models.TextField()
    overview = RichTextField()
    body = StreamField([
        ('section', SectionBlock())
    ])
    listing_abstract = models.TextField()

    search_fields = Page.search_fields + [
        SearchField('introductory_headline'),
        SearchField('overview'),
        SearchField('listing_abstract'),
        SearchField('body')
    ]

    content_panels = Page.content_panels + [
        FieldPanel('introductory_headline', classname='full'),
        FieldPanel('overview'),
        StreamFieldPanel('body'),
    ]

    promote_panels = Page.promote_panels + [
        FieldPanel('listing_abstract')
    ]

    subpage_types = []
