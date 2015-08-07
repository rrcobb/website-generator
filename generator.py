# Write your code here!
def create_element(el_type, contents='', attributes={}):
    elem =  '<' + el_type
    for attribute,value in attributes.iteritems():
        elem += ' '+ attribute + "='" + value + "'"
    elem = elem + '>' + contents + '</' + el_type + '>'
    return elem

def create_void_element(el_type, attributes={}):
    elem =  '<' + el_type
    for attribute,value in attributes.iteritems():
        elem += ' '+ attribute + "='" + value + "'"
    elem = elem + ' />'
    return elem

def create_paragraph(content):
    return create_element("p",content)

def create_header(content,value):
    if value >= 1 and value <= 6:
        tag = 'h' + str(value)
        return create_element(tag,content)
    else:
        return content

def create_link(content, target):
    return create_element('a',content,{'href':target})

def create_image(src, alt=None):
    if alt:
        return create_void_element("img",{'src':src,'alt':alt})
    else:
        return create_void_element("img",{'src':src})

def create_div(content,div_class=None,div_id=None):
    if div_class and div_id:
        attrs = {'class':div_class,'id':div_id}
    elif div_class:
        attrs = {'class':div_class}
    elif div_id:
        attrs = {'id':div_id}
    else:
        attrs = {}
    return create_element("div", content, attrs)

def create_body(content):
    return create_element('body',content)

def create_head(content):
    return create_element('head',content)

def create_page(content):
    return "<!DOCTYPE html>" + create_element('html', content)
