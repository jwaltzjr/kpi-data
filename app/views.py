from flask import render_template

from app import app
from .forms import InputForm

@app.route('/', methods=['GET','POST'])
def index():
    form = InputForm()
    return render_template(
        'index.html',
        title = 'KPI Data Entry',
        form = form
    )
