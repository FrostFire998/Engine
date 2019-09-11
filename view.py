from app import app
from flask import render_template

#вроде как контроллер , данная функция рендерит шаблон по путик к корню сайта
@app.route('/')
def index():
    return render_template('First.html')