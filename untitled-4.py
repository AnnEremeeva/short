from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<string:page_name>/')
def render_static(page_name):
    return render_template('%s.html' % page_name)

if __name__ == '__main__':
    app.run()
    
    
    
    from flask import Flask, abort, redirect, url_for
    app = Flask(__name__)
    
    b = 'https://recyclemap.ru/'
    
    import random
    a = ''
    for i in range (0, 10):
        a = a+random.choice('AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz')
    
    d = {'wiki': 'https://ru.wikipedia.org', 'google': 'https://google.com', 'abc123': 'https://my.site.ru'}
    
    print(a)
    
    d[a] = b
    
    @app.route('/<ip>')
    def index(ip):
        return redirect(d[ip])
    
    
    
    from flask import Flask, render_template
    
    app = Flask(__name__)
    
    @app.route('/<string:page_name>/')
    def render_static(page_name):
        return render_template('%s.html' % page_name)
    
    if __name__ == '__main__':
        app.run()    