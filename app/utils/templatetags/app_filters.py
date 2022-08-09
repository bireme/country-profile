from django import template

register = template.Library()

@register.filter
def substring_after(text, delim):
    return text.partition(delim)[2]


@register.filter
def substring_before(text, delim):
    return text.partition(delim)[0]


@register.filter
def has_data(indicator_list, indicator):
    has_data = True if indicator in indicator_list else False

    return has_data


@register.filter
def display_reference_list(indicator_dict, domain):
    ref_out_list = []

    for indicator_code, indicator_list in indicator_dict.items():
        # get domain number of indicator code. ex. C13.1 == 13 domain
        indicator_domain = int(indicator_code[1:indicator_code.index('.')])

        for indicator in indicator_list:
            if indicator_domain == domain.number and indicator.reference:
                ref_out_list.append("<li>{}: {}</li>".format(indicator.reference_number, indicator.reference))

    ref_out = '\n'.join(ref_out_list)

    return ref_out


@register.filter
def display_data(indicator_list, indicator):
    indicator_data = indicator_list.get(indicator, "")

    paho_data = []
    public_data = []
    for indicator in indicator_data:
        indicator_out = "{}<sup>{}</sup>".format(indicator, indicator.reference_number) if indicator.reference_number else str(indicator)
        if indicator.type == 1:
            paho_data.append(indicator_out)
        else:
            public_data.append(indicator_out)


    table_columns_out = '<td>' + '<br/>'.join(paho_data) + '</td>\n<td>' + '<br/>'.join(public_data) + '</td>'

    return table_columns_out

@register.filter
def get_country_indicator_id(indicator_list, indicator):
    country_indicator_id = indicator_list.get(indicator, "")

    return country_indicator_id