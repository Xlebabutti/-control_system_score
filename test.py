var = "{'qwe': 'asd '}"

def razv(var):
    print(type(var))
    a = var.split(':')
    a1 = eval(a[0].replace('{', '')).strip()

razv(var)


from website import db
>>> from website.extensions import db 
>>> from website import create_app
>>> from website.models import * 
>>> db.create_all(app=create_app())