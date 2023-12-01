from django import template

register = template.Library()

@register.filter(name='limit_words')
def limit_words(value, arg):
    words = value.split()
    limit = int(arg)
    if len(words) > limit:
        words = words[:limit]
        words.append('...')  # Tambahkan elipsis (...) untuk menunjukkan bahwa ada lebih banyak kata
    return ' '.join(words)
