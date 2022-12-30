def domain_name(url):
    domain = url.split('//')
    res = domain[1].split('/')
    return res[0]