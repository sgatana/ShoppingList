from flask_script import Manager

from app import App
app = App()
manager = Manager(app)

if __name__ == '__main__':
    manager.run()