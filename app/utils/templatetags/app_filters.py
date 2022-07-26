from django import template

register = template.Library()

@register.filter
def substring_after(text, delim):
    return text.partition(delim)[2]


@register.filter
def substring_before(text, delim):
    return text.partition(delim)[0]


@register.filter
def get_paho_data(indicator_list, indicator):
    indicator_key = "{}-1".format(indicator)
    indicator_value = indicator_list.get(indicator_key, "")

    return indicator_value

@register.filter
def get_public_data(indicator_list, indicator):
    indicator_key = "{}-2".format(indicator)
    indicator_value = indicator_list.get(indicator_key, "")

    return indicator_value