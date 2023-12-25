from flask import Flask

app = Flask('app')

class app_settings():
    user = 'xxx'
    password = 'xxx'
    database = 'xxx'
    app.config['SQLALCHEMY_DATABASE_URI'] =\
        f"postgresql://{user}:{password}@localhost:5432/{database}"

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = False
    app.config["SECRET_KEY"] = "sdf6as5df67sad54sa"


app.config.from_object(app_settings)

