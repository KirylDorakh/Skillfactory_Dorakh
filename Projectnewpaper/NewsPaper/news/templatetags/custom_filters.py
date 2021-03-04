from django import template

register = template.Library()

CURSE_WORDS = [
    'блядь',
    'хуй',
    'пизда',
]


@register.filter(name='censor')  # регестрируем наш фильтр,
# чтоб django понимал, что это именно фильтр, а не простая функция
def censor(text):  # первый аргумент здесь это то значение, к которому надо применить фильтр,
    # второй аргумент — это аргумент фильтра, т.е. примерно следующее будет в шаблоне value|censor:arg
    words = text.split(' ')
    for word in words:
        if word in CURSE_WORDS:
            index = words.index(word)
            length = len(word)
            words[index] = '*' * length
    text = ' '.join(words)
    return text  # возвращаемое функцией значение — это то значение, которой подставится к нам в шаблон
