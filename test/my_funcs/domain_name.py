def domain_name(url):
    if url.find('/') != -1:
        domain = url.split('//')
        res = domain[1].split('/')
        name = res[0].split('.')
        return name[0]
    else:
        domain = url.split('.')
        if domain[0] == 'www':
            return domain[1]
        else:
            return domain[0]



