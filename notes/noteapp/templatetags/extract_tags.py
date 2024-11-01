from django import template

register = template.Library()

@register.filter
def tags(note_tags):
    return ', '.join([str(name) for name in note_tags.all()])


register.filter('tags', tags)
