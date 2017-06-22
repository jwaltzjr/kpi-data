from flask import render_template, url_for, flash, redirect, request
from werkzeug import MultiDict

from app import app
from . import forms, models

@app.route('/')
def index():
    return render_template(
        'index.html',
        title = 'KPI Data'
    )

@app.route('/add', methods=['GET','POST'])
def add():
    form = forms.InputForm()
    if form.validate_on_submit():
        month_data = models.MonthData(
            form.miles.data,
            form.avg_drivers.data,
            month = form.month.data,
            year = form.year.data,
        )
        month_data.insert()
        flash('Month {} has been saved.'.format(month_data))
        return redirect(url_for('index'))
    return render_template(
        'add.html',
        title = 'Add Entry - KPI Data',
        form = form
    )

@app.route('/edit/<id>', methods=['GET','POST'])
def edit(id):
    month_data = models.MonthData.fetch(id)
    if request.method == 'POST':
        form = forms.InputForm()
        if form.validate_on_submit():
            month_data.miles = form.miles.data
            month_data.avg_drivers = form.avg_drivers.data
            month_data.update()
            flash('Month {} has been saved.'.format(month_data))
            return redirect(url_for('index'))
    elif request.method == 'GET':
        formdata = MultiDict({
            'month': month_data.month_id[:2],
            'year': month_data.month_id[-4:],
            'miles': month_data.miles,
            'avg_drivers': month_data.avg_drivers
        })
        form = forms.InputForm(formdata=formdata)
        flash(month_data)
    return render_template(
        'add.html',
        title = 'Add Entry - KPI Data',
        form = form
    )

@app.route('/history')
def history():
    data = models.MonthData.fetchall()
    return render_template(
        'history.html',
        title = 'History - KPI Data',
        data = data
    )
