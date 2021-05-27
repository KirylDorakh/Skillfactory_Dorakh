from django import template
import datetime

register = template.Library()

@register.filter(name='censor')
def multiply(value):
    curce = ['fuck', 'fucked', 'fucking', 'nigger', 'niggers', 'whore', 'whores', 'slut', 'sluts',
             'bitch', 'freak', 'douchebag', 'faggot', 'homo', 'prick', 'dick', 'cunt', 'pussy']
    value = value.lower().replace(',', '').replace('.', '').split()
    result = []

    for word in value:
        if word not in curce:
            result.append(word)
        else:
            result.append('*' *len(word))
    result = ' '.join(result)
    return result

@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)


@register.filter
def hide_forbidden(value):
    words = value.split()
    result = []
    forbidden_words = ['fuck', 'fucked', 'fucking', 'nigger', 'niggers', 'whore', 'whores', 'slut', 'sluts',
             'bitch', 'freak', 'douchebag', 'faggot', 'homo', 'prick', 'dick', 'cunt', 'pussy']
    for word in words:
        if word in forbidden_words:
            result.append(word[0] + "*"*(len(word)-2) + word[-1])
        else:
            result.append(word)
    return " ".join(result)