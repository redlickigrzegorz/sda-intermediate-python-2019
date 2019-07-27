def tag(name, *content, cls=None, **attrs):
    """Generate one or more HTML tags"""
    if cls is not None:
        attrs["class"] = cls
    if attrs:
        attr_str = "".join(f' {attr}="{value}"'
                           for attr, value
                           in sorted(attrs.items()))
    else:
        attr_str = ""
    if content:

        return "\n".join(f'<{name}{attr_str}>{c}</{name}>'
                         for c in content)
    else:
        return f'<{name}{attr_str} />'


if __name__ == '__main__':
    print(tag('Marian','Rudy', 'Wysoki', 'Biedny', 'Bezrobotny' , cls="Koalski", wiek=25))

    t = {"wiek": 25, "cls" : 'Koalski'}
    print(tag('Marian','Rudy', 'Wysoki', 'Biedny', 'Bezrobotny' , **t ))
