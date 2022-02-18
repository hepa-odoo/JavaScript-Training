import os
import redis
from werkzeug.urls import url_parse
from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.middleware.shared_data import SharedDataMiddleware
from werkzeug.utils import redirect
from jinja2 import Environment, FileSystemLoader
from rpc0.odooRPC import odooGetData
from backend.register_in_database import register_in_database_func
from backend.get_customers import get_customers_func

class App(object):

    def __init__(self, config):
        self.redis = redis.Redis(config['redis_host'], config['redis_port'], decode_responses=True)
        template_path = os.path.join(os.path.dirname(__file__), 'templates')
        self.jinja_env = Environment(loader=FileSystemLoader(template_path),autoescape=True)
        
        self.url_map = Map([
            Rule('/', endpoint='index'),
            Rule('/task1', endpoint='Events0'),
            Rule('/date', endpoint='date0'),
            Rule('/task2', endpoint='asyncAwait0'),
            Rule('/odooGetData', endpoint='odooGetData0'),
            Rule('/register', endpoint='register0'),
            Rule('/registerInDatabase', endpoint='registerInDatabase0'),
            Rule('/getCustomers', endpoint='getCustomers0')
        ])

    def on_index(self, request):
        return self.render_template('index.html',render_context={})

    def on_Events0(self, request):
        return self.render_template('Events0.html',render_context={})
    
    def on_date0(self, request):
        return self.render_template('dates.html',render_context={})
    
    def on_asyncAwait0(self, request):
        return self.render_template('asyncAwait.html',render_context={})
    
    def on_odooGetData0(self, request):
        return Response(odooGetData(), mimetype='application/json')
        #return self.render_template('rpcRenderer.html',render_context={'odooData':odooData})
    
    def on_register0(self, request):
        return self.render_template('register.html',render_context={})

    def on_registerInDatabase0(self, request): 
        fname=request.form["fname"]
        lname=request.form["lname"]
        email=request.form["email"]
        password=request.form["password"]
        return Response(register_in_database_func(fname,lname,email,password), mimetype='text/plain')
    
    def on_getCustomers0(self, request):
        return Response(get_customers_func(), mimetype='text/html')

    def render_template(self, template_name, **context):
        t = self.jinja_env.get_template(template_name)
        return Response(t.render(context.get('render_context')), mimetype='text/html')

    def dispatch_request(self, request):
        adapter = self.url_map.bind_to_environ(request.environ)
        try:
            endpoint, values = adapter.match()
            return getattr(self, f'on_{endpoint}')(request, **values)
        except HTTPException as e:
            return e

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)


def create_app(redis_host='localhost', redis_port=8000, with_static=True):
    app = App({
        'redis_host':       redis_host,
        'redis_port':       redis_port
    })
    if with_static:
        app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
            '/static':  os.path.join(os.path.dirname(__file__), 'static')
        })
    return app

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    app = create_app()
    run_simple('127.0.0.1', 8000, app, use_debugger=True, use_reloader=True)