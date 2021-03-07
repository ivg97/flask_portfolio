from app_portfolio import app


@app.route('/')
@app.route('/index')
def index():
    '''Main page'''
    return f'Hello, World!'