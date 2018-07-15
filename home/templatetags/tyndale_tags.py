from django import template
from home.models import *


register = template.Library()


@register.simple_tag(takes_context=True)
def get_site_root(context):
    return context['request'].site.root_page


@register.inclusion_tag("home/inclusion/header.html", takes_context=True)
def display_navbar(context, parent, calling_page=None):
    menuitems = parent.get_children().live().in_menu()
    for menuitem in menuitems:
        menuitem.has_children = menuitem.get_children().live().in_menu().exists()
        menuitem.active = (calling_page.url.startswith(menuitem.url) if calling_page else False)

    return {
        "calling_page": calling_page,
        "menuitems": menuitems,
        "request": context['request']
    }


@register.inclusion_tag("home/inclusion/footer.html", takes_context=True)
def display_footer(context, calling_page=None):

    return {
        "calling_page": calling_page,
        "request": context['request'],
    }


@register.inclusion_tag("home/inclusion/breadcrumbs.html", takes_context=True)
def display_breadcrumbs(context, calling_page=None):
    current_page = context['self']
    ancestors = current_page.get_ancestors().exclude(title='Root')
    return {
        "ancestors": ancestors,
        "current_page": calling_page,
    }


@register.inclusion_tag("home/inclusion/sidemenu.html", takes_context=True)
def display_sidemenu(context, calling_page=None):
    current_page = context['self']
    has_children = current_page.get_children().live().in_menu().exists()
    menuitems_children = current_page.get_children().live().in_menu()

    ancestor = current_page.get_ancestors().last()
    if ancestor is not None:
        ancestor_children_has_children = ancestor.get_children().live().in_menu().exists()
        if ancestor_children_has_children:
            ancestor_children = ancestor.get_children().live().in_menu()
        else:
            ancestor_children = ()
    else:
        ancestor_children_has_children = False
        ancestor_children = ()

    return {
        "ancestor": ancestor,
        "ancestor_children_has_children": ancestor_children_has_children,
        "ancestor_children": ancestor_children,
        "current_page": current_page,
        "children": menuitems_children,
        "has_children": has_children,
        "request": context['request']
    }


@register.inclusion_tag("home/inclusion/staffs.html", takes_context=True)
def display_staffs(context):
    return {
        "staffs": Staff.objects.all().order_by('order_number'),
        'request': context['request'],
    }


@register.inclusion_tag("home/inclusion/academic_program_list.html", takes_context=True)
def display_academic_list(context):
    current_page = context['self']
    #children = current_page.get_children().live()
    children = AcademicProgramDetailPage.objects.all().live().order_by('order_number')
    # TODO
    # order by number

    return {
        "children": children,
        "request": context['request'],
    }


@register.inclusion_tag("home/inclusion/faculty.html", takes_context=True)
def display_faculty(context):
    current_page = context['self']
    children = FacultyDetailPage.objects.all().live().order_by('order_number')

    return {
        "children": children,
        "request": context['request'],
    }


@register.inclusion_tag("home/inclusion/semester.html", takes_context=True)
def display_semester(context):
    current_page = context['self']
    return {
        "children": current_page.get_children().live(),
        "request": context['request'],
    }


@register.inclusion_tag("home/inclusion/course.html", takes_context=True)
def display_course(context):
    current_page = context['self']
    return {
        "children": current_page.get_children().live(),
        "request": context['request'],
    }


@register.inclusion_tag("home/inclusion/latest_post.html", takes_context=True)
def display_latest_post(context):
    return {
        "posts": CourseDetailPage.objects.all().order_by('-upload_date')[:5],
        "request": context['request']
    }


@register.inclusion_tag("home/inclusion/foorter_menu.html", takes_context=True)
def display_footer_menu(context, parent, calling_page=None):

    menuitems = parent.get_children().live().in_menu()
    for menuitem in menuitems:
        menuitem.has_children = menuitem.get_children().live().in_menu().exists()
        menuitem.active = (calling_page.url.startswith(menuitem.url) if calling_page else False)

    return {
        "calling_page": calling_page,
        "menuitems": menuitems,
        "request": context['request']
    }
