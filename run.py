from flask_script import Manager

from app.views import app
App = app()
manager = Manager(App)

if __name__ == '__main__':
    manager.run()