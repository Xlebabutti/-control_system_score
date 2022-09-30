var = "{'qwe': 'asd '}"

def razv(var):
    print(type(var))
    a = var.split(':')
    a1 = eval(a[0].replace('{', '')).strip()

razv(var)