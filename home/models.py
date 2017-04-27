from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, FieldRowPanel, InlinePanel, MultiFieldPanel
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtailforms.models import AbstractEmailForm, AbstractFormField
from wagtail.wagtailforms.edit_handlers import FormSubmissionsPanel
from modelcluster.fields import ParentalKey


class HomePage(Page):
    overlay_banner_title_1 = models.TextField(default="Your Career starts here")
    overlay_banner_description_1 = RichTextField(default="Description")
    overlay_banner_thumb_image_1 = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="150x150 pixel image"
    )

    overlay_banner_title_2 = models.TextField(default="Your Career starts here")
    overlay_banner_description_2 = RichTextField(default="Description")
    overlay_banner_thumb_image_2 = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="150x150 pixel image"
    )

    overlay_banner_title_3 = models.TextField(default="Your Career starts here")
    overlay_banner_description_3 = RichTextField(default="Description")
    overlay_banner_thumb_image_3 = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="150x150 pixel image"
    )

    overlay_banner_title_4 = models.TextField(default="Your Career starts here")
    overlay_banner_description_4 = RichTextField(default="Description")
    overlay_banner_thumb_image_4 = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="150x150 pixel image"
    )

    slider_image_1 = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="1920x1280 pixel image"
    )

    slider_banner_title_1 = models.TextField(default="For a better education")
    slider_banner_description_1 = RichTextField(default="description")

    slider_image_2 = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="1920x1280 pixel image"
    )

    slider_banner_title_2 = models.TextField(default="For a better education")
    slider_banner_description_2 = RichTextField(default="description")

    about_tiu_title = models.TextField(default="About TIU")
    about_tiu_description = RichTextField(default="Description of TIU")

    state_mission_title = models.TextField(default="Statement of Mission")
    state_mission_description = RichTextField(default="Description of mission")

    state_faith_title = models.TextField(default="Statement of Faith")
    state_faith_description = RichTextField(default="Description of Faith")

    our_mission_title = models.TextField(default="Preparing students to serve Christ and his church through biblical, experiential, and practical ministry")

    president_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="342 x 478 pixels"
    )
    president_title = models.TextField(default="President's Welcome")
    president_message = RichTextField(default="Description")

    chairman_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="342 x 478 pixels"
    )
    chairman_title = models.TextField(default="Chairman's Welcome")
    chairman_message = RichTextField(default="Message")

    tyndale_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="342 x 478 pixels"
    )
    tyndale_title = models.TextField(default="Learn about Tyndale")
    tyndale_message = RichTextField(default="Message")

    yala_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="342 x 478 pixels"
    )
    yala_title = models.TextField(default="Learn about Yala")
    yala_message = RichTextField(default="message")


    content_panels = Page.content_panels + [
        ImageChooserPanel('slider_image_1'),
        FieldPanel('slider_banner_title_1'),
        FieldPanel('slider_banner_description_1'),

        ImageChooserPanel('slider_image_2'),
        FieldPanel('slider_banner_title_2'),
        FieldPanel('slider_banner_description_2'),

        FieldPanel('overlay_banner_title_1'),
        FieldPanel('overlay_banner_description_1'),
        ImageChooserPanel('overlay_banner_thumb_image_1'),

        FieldPanel('overlay_banner_title_2'),
        FieldPanel('overlay_banner_description_2'),
        ImageChooserPanel('overlay_banner_thumb_image_2'),

        FieldPanel('overlay_banner_title_3'),
        FieldPanel('overlay_banner_description_3'),
        ImageChooserPanel('overlay_banner_thumb_image_3'),

        FieldPanel('overlay_banner_title_4'),
        FieldPanel('overlay_banner_description_4'),
        ImageChooserPanel('overlay_banner_thumb_image_4'),

        FieldPanel('about_tiu_title'),
        FieldPanel('about_tiu_description'),
        FieldPanel('state_mission_title'),
        FieldPanel('state_mission_description'),
        FieldPanel('state_faith_title'),
        FieldPanel('state_faith_description'),

        FieldPanel('our_mission_title'),
        ImageChooserPanel('president_image'),
        FieldPanel('president_title'),
        FieldPanel('president_message'),
        ImageChooserPanel('chairman_image'),
        FieldPanel('chairman_title'),
        FieldPanel('chairman_message'),
        ImageChooserPanel('tyndale_image'),
        FieldPanel('tyndale_title'),
        FieldPanel('tyndale_message'),
        ImageChooserPanel('yala_image'),
        FieldPanel('yala_title'),
        FieldPanel('yala_message'),
    ]