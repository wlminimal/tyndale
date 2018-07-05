from __future__ import absolute_import, unicode_literals

from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, FieldRowPanel, InlinePanel, MultiFieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet
# from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
# from wagtail.contrib.forms.edit_handlers import FormSubmissionsPanel

from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.contrib.forms.edit_handlers import FormSubmissionsPanel
from wagtail.core.blocks import TextBlock, CharBlock, RichTextBlock, StreamBlock
from wagtail.images.blocks import ImageChooserBlock

from modelcluster.fields import ParentalKey


@register_snippet
class Popup(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField(default="Some News")

    def __str__(self):
        return self.title


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


@register_snippet
class Quote(models.Model):
    quote_message = RichTextField(default="quote_message")
    quote_speaker = models.CharField(max_length=50, default="Taehwan Kim")
    quote_speaker_title = models.CharField(max_length=100, default="Senior Pastor")
    quote_profile_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="50x50 pixels image"
    )

    def __str__(self):
        return self.quote_speaker


class HomepageQuotes(Orderable, models.Model):
    page = ParentalKey('home.HomePage', related_name='home_quote')
    quote = models.ForeignKey('home.Quote', null=True, related_name='+', on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "Quote for Homepage"
        verbose_name_plural = "Quotes for Homepage"

    panels = [
        SnippetChooserPanel('quote')
    ]

    def __str__(self):
        return self.page.title + " --> " + self.quote.quote_speaker


@register_snippet
class SliderMessage(models.Model):
    title = models.CharField(max_length=100, default="Good is good")
    message = RichTextField(default="Message")
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="150x150 pixel"
    )

    def __str__(self):
        return self.title


class HomepageSliderMessages(Orderable, models.Model):
    page = ParentalKey('home.HomePage', related_name='slider_message')
    message = models.ForeignKey('home.SliderMessage', null=True, related_name='+', on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "Message for slider"
        verbose_name_plural = "Messages for slider"

    panels = [
        SnippetChooserPanel('message')
    ]

    def __str__(self):
        return self.page.title + " --> " + self.message.title


class HomePage(Page):

    slider_image_1 = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="1920x1280 pixel image"
    )

    slider_image_2 = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="1920x1280 pixel image"
    )

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

    grid_title = models.CharField(max_length=100, default="Academic Programs")
    grid_subtitle = models.TextField(default="Description of grid item")
    grid_link_page = models.ForeignKey(
        "wagtailcore.Page",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    popup = models.ForeignKey(
        "home.Popup",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    @property
    def academics(self):
        academics = AcademicProgramDetailPage.objects.all().order_by('-order_number')[:6]

        return academics

    def get_context(self, request, *args, **kwargs):
        academics = self.academics
        context = super(HomePage, self).get_context(request, *args, **kwargs)
        context['academics'] = academics

        return context

    content_panels = Page.content_panels + [

        SnippetChooserPanel('popup'),
        ImageChooserPanel('slider_image_1'),

        ImageChooserPanel('slider_image_2'),

        InlinePanel('slider_message', label="Message in Slider"),

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
        FieldPanel('grid_title'),
        FieldPanel('grid_subtitle'),
        PageChooserPanel('grid_link_page'),
        InlinePanel('home_quote', label="Quotes"),

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


@register_snippet
class Professor(models.Model):
    profile_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null= True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Professor profile picture( square image recommended )"
    )

    name = models.CharField(max_length=100, default="Professor Name")
    profile_page = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        related_name='+',
        on_delete=models.SET_NULL
    )

    @property
    def link(self):
        if self.profile_page:
            return self.profile_page.url
        else:
            None

    def __str__(self):
        return self.name


class CourseDetailPage(Page):
    course_name = models.TextField(default="Ancient Church History")
    course_description = RichTextField(default="Description of course")
    professor_name = models.CharField(max_length=70, default="Professor name")
    video_url = models.CharField(max_length=255, default="PMJFfMWgyZI")
    upload_date = models.DateField(default=datetime.date.today)

    professor = models.ForeignKey(
        "home.Professor",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    content_panels = Page.content_panels + [
        FieldPanel('course_name'),
        FieldPanel('course_description'),
        FieldPanel('professor_name'),
        FieldPanel('video_url'),
        SnippetChooserPanel('professor'),
    ]

    # @property
    # def courses(self):
    #     courses = CourseDetailPage.objects.all()
    #     courses = courses.order_by('-upload_date')
    #
    #     return courses
    #
    # def get_context(self, request, *args, **kwargs):
    #
    #     courses = self.courses
    #
    #     # Pagination
    #     paginator = Paginator(courses, 1)
    #     page = request.GET.get('page')
    #
    #     try:
    #         courses = paginator.page(page)
    #     except PageNotAnInteger:
    #         courses = paginator.page(1)
    #     except EmptyPage:
    #         courses = paginator.page(paginator.num_pages)
    #
    #     context = super(CourseDetailPage, self).get_context(request, *args, **kwargs)
    #     context['paged_courses'] = courses
    #
    #     return context


class AcademicProgramListPage(Page):
    subpage_types = ['home.AcademicProgramDetailPage']


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

    subpage_types = ['home.FacultyDetailPage']


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
    contact_title = models.TextField(default="Tyndale International University")
    address = models.TextField(default="4270 W. 6th St.  Los Angeles,  California  90020")
    phone_number = models.TextField(default="(213) 595-3181")
    website = models.TextField(default="www.tyndaleinternationaluniversity.org / www.yalamission.org")
    emails = models.TextField(default="tiu4270@gmail.com / info.tyndaleinternationaluniversity@gmail.com")
    office_hours = RichTextField(default="Office Hours")
    thank_you_text = RichTextField(default="Thank you for contacting us. We will get back to you soon.")
    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('contact_title'),
        FieldPanel('address'),
        FieldPanel('phone_number'),
        FieldPanel('website'),
        FieldPanel('emails'),
        FieldPanel('office_hours'),
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


class NewsPage(Page):
    greeting = models.TextField(default="틴데일 신학교 게시판에 오신걸 환영합니다.")
    description = RichTextField(default="이곳에서 틴데일 신학교에 대한 새로운 소식을 읽으시길 바랍니다.")

    @property
    def news(self):
        news = NewsDetailPage.objects.filter(featured__exact=False).order_by('-created_at')
        return news

    @property
    def featured_news(self):
        featured_news = NewsDetailPage.objects.filter(featured__exact=True).order_by('-created_at')
        return featured_news

    def get_context(self, request, *args, **kwargs):

        news = self.news
        paginator = Paginator(news, 10)
        page = request.GET.get('page')

        try:
            news = paginator.page(page)
        except PageNotAnInteger:
            news = paginator.page(1)
        except EmptyPage:
            news = paginator.page(paginator.num_pages)

        featured_news = self.featured_news
        context = super(NewsPage, self).get_context(request, *args, **kwargs)
        context['news'] = news
        context['featured_news'] = featured_news

        return context

    subpage_types = ['home.NewsDetailPage']

    content_panels = Page.content_panels + [
        FieldPanel('greeting'),
        FieldPanel('description'),
    ]


class NewsDetailPage(Page):
    news_title = models.CharField(max_length=255, default="News Title")
    news_content = RichTextField(default="News Content")
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    content_panels = Page.content_panels + [
        FieldPanel('news_title'),
        FieldPanel('featured'),
        FieldPanel('news_content')
    ]
