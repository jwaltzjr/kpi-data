from flask import render_template, url_for, flash, redirect, request
from pyodbc import IntegrityError
from werkzeug import MultiDict

from app import app
from . import forms, models

@app.route('/')
def index():
    return render_template(
        'index.html',
        title='KPI Data'
    )

@app.route('/add', methods=['GET','POST'])
def add():
    form = forms.MonthDataAddForm()
    if form.validate_on_submit():
        month_data = models.MonthData(
            form.miles.data,
            form.avg_drivers.data,
            month=form.month.data,
            year=form.year.data,
        )
        try:
            month_data.insert()
        except IntegrityError:
            flash('Month could not be saved - data for this month already exists.')
            return redirect(url_for('add'))
        else:
            flash('Month {} has been saved.'.format(month_data))
            return redirect(url_for('index'))
    return render_template(
        'add.html',
        title='Add Entry - KPI Data',
        form=form
    )

@app.route('/edit/<id>', methods=['GET','POST'])
def edit(id):
    month_data = models.MonthData.fetch(id)
    if request.method == 'POST':
        form = forms.MonthDataUpdateForm()
        if form.validate_on_submit():
            month_data.miles = form.miles.data
            month_data.avg_drivers = form.avg_drivers.data
            month_data.update()
            flash('Month {} has been saved.'.format(month_data))
            return redirect(url_for('index'))
    elif request.method == 'GET':
        formdata = MultiDict({
            'miles': month_data.miles,
            'avg_drivers': month_data.avg_drivers
        })
        form = forms.MonthDataUpdateForm(formdata=formdata)
    return render_template(
        'edit.html',
        title='Add Entry - KPI Data',
        form=form,
        month=month_data.month_id
    )

@app.route('/delete/<id>')
def delete(id):
    month_data = models.MonthData.fetch(id)
    return render_template(
        'delete.html',
        title='Delete Entry - KPI Data',
        month=month_data
    )

@app.route('/delete/<id>/confirmed')
def delete_confirmed(id):
    month_data = models.MonthData.fetch(id)
    month_string = month_data.__repr__()
    month_data.delete()
    flash('Month {} was successfully deleted.'.format(month_string))
    return redirect(url_for('index'))

@app.route('/history')
def history():
    data = sorted(
        models.MonthData.fetchall(),
        key=lambda month: month.month_id,
        reverse=True
    )
    return render_template(
        'history.html',
        title='History - KPI Data',
        data=data
    )
