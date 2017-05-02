from __future__ import absolute_import, unicode_literals

from django.db import models
import datetime

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, FieldRowPanel, InlinePanel, MultiFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtailforms.models import AbstractEmailForm, AbstractFormField
from wagtail.wagtailforms.edit_handlers import FormSubmissionsPanel
from wagtail.wagtailcore.blocks import TextBlock, CharBlock, RichTextBlock, StreamBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock

from modelcluster.fields import ParentalKey


@register_snippet
class Staff(models.Model):
    profile_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="360x360 pixels"
    )
    name = models.CharField(max_length=100, default="Name")
    position = models.CharField(max_length=100, default="Position")
    order_number = models.IntegerField(default=10, blank=False)

    def __str__(self):
        return self.name


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


class AboutPage(Page):
    main_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="1500x650 pixels"
    )
    main_title = models.TextField(default="About Tyndale International University")
    main_description = RichTextField(default="Description")

    content_panels = Page.content_panels + [
        ImageChooserPanel('main_image'),
        FieldPanel('main_title'),
        FieldPanel('main_description'),
    ]


class PresidentWelcomePage(Page):
    profile_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="263x263 pixels"
    )

    name = models.CharField(max_length=100, default="Joen Doe")
    spec = models.CharField(max_length=100, default="Ph.D", help_text="Ph.D, D.D")
    position = models.CharField(max_length=100, default="President", help_text="President")
    message = RichTextField(default="Message")

    content_panels = Page.content_panels + [
        ImageChooserPanel('profile_image'),
        FieldPanel('name'),
        FieldPanel('spec'),
        FieldPanel('position'),
        FieldPanel('message'),
    ]


class ChairmanWelcomePage(Page):
    profile_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="263x263 pixels"
    )

    name = models.CharField(max_length=100, default="Joen Doe")
    spec = models.CharField(max_length=100, default="Ph.D", help_text="Ph.D, D.D")
    position = models.CharField(max_length=100, default="President", help_text="President")
    message = RichTextField(default="Message")

    content_panels = Page.content_panels + [
        ImageChooserPanel('profile_image'),
        FieldPanel('name'),
        FieldPanel('spec'),
        FieldPanel('position'),
        FieldPanel('message'),
    ]


class StateOfFaithPage(Page):
    main_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="1500x650 pixels"
    )
    main_title = models.TextField(default="About Tyndale International University")
    main_description = RichTextField(default="Description")

    content_panels = Page.content_panels + [
        ImageChooserPanel('main_image'),
        FieldPanel('main_title'),
        FieldPanel('main_description'),
    ]


class StateOfMissionPage(Page):
    main_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="1500x650 pixels"
    )
    main_title = models.TextField(default="About Tyndale International University")
    main_description = RichTextField(default="Description")

    content_panels = Page.content_panels + [
        ImageChooserPanel('main_image'),
        FieldPanel('main_title'),
        FieldPanel('main_description'),
    ]


class AdminStaffPage(Page):

    content_panels = Page.content_panels + [

    ]


class AcademicsPage(Page):
    main_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="1500x1000 pixels"
    )
    main_title = models.TextField(default="About Tyndale International University")
    main_description = RichTextField(default="Description")

    content_panels = Page.content_panels + [
        ImageChooserPanel('main_image'),
        FieldPanel('main_title'),
        FieldPanel('main_description'),
    ]


class CourseDescriptionPage(Page):
    main_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="1500x1000 pixels"
    )
    main_title = models.TextField(default="About Tyndale International University")
    main_description = RichTextField(default="Description")

    content_panels = Page.content_panels + [
        ImageChooserPanel('main_image'),
        FieldPanel('main_title'),
        FieldPanel('main_description'),
    ]


class SemesterIndexPage(Page):
    semester_title = models.CharField(max_length=100, default="Choose Semester")
    semester_subtitle = models.TextField(default="Here is our all course")

    content_panels = Page.content_panels +[
        FieldPanel('semester_title'),
        FieldPanel('semester_subtitle'),
    ]

    subpage_types = ['home.SemesterPage']


# display course list in semester
class SemesterPage(Page):
    semester_name = models.CharField(max_length=100, default="Choose Semester")
    thumb_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="500 x 500 image for semester index page "
    )
    start_month = models.CharField(max_length=40, default="Mar")
    start_date = models.CharField(max_length=40, default="27")

    @property
    def courses(self):
        courses = CourseListPage.objects.live().descendant_of(self)
        return courses

    def get_context(self, request, *args, **kwargs):
        courses = self.courses
        context = super(SemesterPage, self).get_context(request, *args, **kwargs)
        context['courses'] = courses

        return context

    content_panels = Page.content_panels + [
        FieldPanel('semester_name'),
        FieldPanel('start_month'),
        FieldPanel('start_date'),
        ImageChooserPanel('thumb_image'),

    ]

    subpage_types = ['home.CourseListPage']


class CourseListPage(Page):
    course_name = models.TextField(default="Course Name")
    course_intro = RichTextField(default="Brief introduction of course")
    thumb_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="500 x 500 image for course intro page "
    )

    @property
    def course_url(self):
        # Find closest descendent which is Course List
        course = CourseListPage.objects.live().descendant_of(self)
        return course

    def get_context(self, request, *args, **kwargs):
        course_url = self.course_url

        context = super(CourseListPage, self).get_context(request, *args, **kwargs)
        context['course_url'] = course_url

        return context

    content_panels = Page.content_panels + [
        FieldPanel('course_name'),
        FieldPanel('course_intro'),
        ImageChooserPanel('thumb_image'),
    ]

    parent_page_types = ['home.SemesterPage']
    subpage_types = ['home.CourseDetailPage']


class CourseDetailPage(Page):
    course_name = models.TextField(default="Ancient Church History")
    course_description = RichTextField(default="Description of course")
    professor_name = models.CharField(max_length=70, default="Professor name")
    video_url = models.URLField(default="http://www.youtube.com")
    upload_date = models.DateField(default=datetime.date.today)

    content_panels = Page.content_panels + [
        FieldPanel('course_name'),
        FieldPanel('course_description'),
        FieldPanel('professor_name'),
        FieldPanel('video_url'),
    ]


class AcademicProgramListPage(Page):
    pass


class AcademicProgramDetailPage(Page):
    academic_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="265x265 pixels"
    )

    academic_name = models.TextField(default="Academic Program Name")
    start_date = models.CharField(max_length=100, default="March 11, 2017")
    duration = models.CharField(max_length=50, default="8 weeks")
    academic_description = RichTextField(default="Academic Program Description")
    order_number = models.IntegerField(default=10)

    content_panels = Page.content_panels + [
        FieldPanel('academic_name'),
        ImageChooserPanel('academic_image'),
        FieldPanel('start_date'),
        FieldPanel('duration'),
        FieldPanel('academic_description'),
        FieldPanel('order_number'),

    ]


class FacultyPage(Page):
    pass


class FacultyDetailPage(Page):
    profile_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="360x360 pixels"
    )
    name = models.CharField(max_length=100, default="Name")
    spec = RichTextField(default="Spec of professor")
    class_name = models.TextField(default="class name")
    order_number = models.IntegerField(default=10, blank=False)

    content_panels = Page.content_panels + [
        ImageChooserPanel('profile_image'),
        FieldPanel('name'),
        FieldPanel('spec'),
        FieldPanel('class_name'),
        FieldPanel('order_number'),

    ]


class AdmissionPage(Page):
    main_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="1500x1000 pixels"
    )
    main_title = models.TextField(default="About Tyndale International University")
    main_description = RichTextField(default="Description")

    content_panels = Page.content_panels + [
        ImageChooserPanel('main_image'),
        FieldPanel('main_title'),
        FieldPanel('main_description'),
    ]


class TuitionInfoPage(Page):
    main_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="1500x1000 pixels"
    )
    main_title = models.TextField(default="About Tyndale International University")
    main_description = RichTextField(default="Description")

    content_panels = Page.content_panels + [
        ImageChooserPanel('main_image'),
        FieldPanel('main_title'),
        FieldPanel('main_description'),
    ]


class FormField(AbstractFormField):
    page = ParentalKey('ContactPage', related_name='form_fields')


class ContactPage(AbstractEmailForm):
    thank_you_text = RichTextField(default="Thank you for contacting us. We will get back to you soon.")
    content_panels = AbstractEmailForm.content_panels + [
        FormSubmissionsPanel(),
        InlinePanel('form_fields', label='Contact Form Fields'),
        FieldPanel('thank_you_text', classname='full'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname='col6'),
                FieldPanel('to_address', classname='col6'),
            ]),
            FieldPanel('subject'),
        ], 'Email'),
    ]





























