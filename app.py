from settings import app
from models import db
from views import UserAPI, AdvirtisementsAPI

if __name__ == "__main__":
    @app.before_first_request
    def create_table():
        db.create_all()

    app.add_url_rule('/users/<user_id>', view_func=UserAPI.as_view('user'))
    app.add_url_rule('/users/', view_func=UserAPI.as_view('users'))
    app.add_url_rule('/adv/<adv_id>', view_func=AdvirtisementsAPI.as_view('adv'))
    app.add_url_rule('/adv/', view_func=AdvirtisementsAPI.as_view('advs'))

    app.run(host='localhost', port=8000)