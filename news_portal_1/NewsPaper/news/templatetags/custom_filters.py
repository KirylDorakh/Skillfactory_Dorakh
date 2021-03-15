from django import template

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

