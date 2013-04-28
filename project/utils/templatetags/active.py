# http://stackoverflow.com/a/656328/170172

from django import template

register = template.Library()


@register.tag
def active(parser, token):
    args = token.split_contents()
    template_tag = args[0]
    if len(args) < 2:
        raise (
            template.TemplateSyntaxError,
            "%r tag requires at least one argument" % template_tag
        )
    return NavSelectedNode(args[1])


class NavSelectedNode(template.Node):
    def __init__(self, url):
        self.url = url

    def render(self, context):
        path = context['request'].path
        pValue = template.Variable(self.url).resolve(context)
        if path == pValue:
            return 'active'
        return ""
