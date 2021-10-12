import os
from flask import Flask, jsonify, redirect
from .utils.extensions import scheduler
from .blueprints import stocks, crypto
from .utils.api_spec import spec
from .utils.swagger import swagger_ui_blueprint, SWAGGER_URL


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    scheduler.init_app(app)
    scheduler.start()

    app.register_blueprint(stocks.bp)
    app.register_blueprint(crypto.bp)

    with app.app_context():
        # register all swagger documented functions here
        for fn_name in app.view_functions:
            if fn_name == 'static':
                continue
            print(f"Loading swagger docs for function: {fn_name}")
            view_fn = app.view_functions[fn_name]
            spec.path(view=view_fn)
    
    @app.route("/swagger.json")
    def create_swagger_spec():
        return jsonify(spec.to_dict())

    @app.route('/')
    def entry():
        return redirect('/api')

    app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

    return app
