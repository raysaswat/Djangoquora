from django import template

register = template.Library()

@register.simple_tag
def has_upvoted(user, answer):
    return user.id in list(answer.upvote_set.all().values_list("user", flat=True))