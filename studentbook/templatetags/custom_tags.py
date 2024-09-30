from django import template

register = template.Library()  # Call the function to create an instance

@register.simple_tag
def get_half_content(description):
    '''
    "harinarayan" => 11
    half of 11 is 5.5, which is "hari"
    
    :param description: The string whose half-content is to be returned
    :return: Half of the given string
    '''
    
    return description[:int(len(description)/2)]
    # total = len(description)
    # half = total / 2
    # half = int(half)
    
    # content = description[:half]
    # return content
