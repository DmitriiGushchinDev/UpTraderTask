from django.template import RequestContext
from django.templatetags.cache import register
from django import template
from Menu.models import MenuItem

register = template.Library()

@register.inclusion_tag('menu/draw_menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    path = request.path

    all_items = MenuItem.objects.filter(menu_name=menu_name).select_related('parent').prefetch_related('children')

    items_by_id = {item.id: item for item in all_items}
    root_items = []

    active_item = next((item for item in all_items if item.get_url() == path), None)

    expanded_ids = set()
    if active_item:
        current = active_item
        while current:
            expanded_ids.add(current.id)
            current = current.parent

    for item in all_items:
        item.children_list = []
    for item in all_items:
        if item.parent_id:
            items_by_id[item.parent_id].children_list.append(item)
        else:
            root_items.append(item)
    
    return {
        'menu_items': root_items,
        'expanded_ids': expanded_ids,
        'current_path': path,
    }