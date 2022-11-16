# -*- coding: UTF-8 -*-

import web

urls = (
    '/testovoe', 'HelloRekruto',
)
app = web.application(urls, globals())
render = web.template.render('templates/')


class HelloRekruto(object):

    def GET(self):
        i = web.input(name=None, message=None)
        return render.index(i.name, i.message)


if __name__ == "__main__":
    app.run()
