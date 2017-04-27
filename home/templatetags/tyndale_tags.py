from django import template


register = template.Library()


@register.assignment_tag(takes_context=True)
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
    }


@register.inclusion_tag("home/inclusion/breadcrumbs.html", takes_context=True)
def display_breadcrumbs(context, calling_page=None):
    ancestors = calling_page.get_ancestors().exclude(title='Root')
    return {
        "ancestors": ancestors,
        "current_page": calling_page,
    }