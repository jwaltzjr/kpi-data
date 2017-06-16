from flask import render_template, url_for, flash, redirect

from app import app
from . import forms, models

@app.route('/', methods=['GET','POST'])
def index():
    form = forms.InputForm()
    if form.validate_on_submit():
        month_data = models.MonthData(
            form.month.data,
            form.year.data,
            form.miles.data,
            form.avg_drivers.data
        )
        flash('Month {} has been saved.'.format(month_data))
        return redirect(url_for('index'))
    return render_template(
        'index.html',
        title = 'KPI Data Entry',
        form = form
    )

@app.route('/history')
def history():
    data = models.MonthData.fetchall()
    return render_template(
        'history.html',
        title = 'KPI Data History',
        data = data
    )
