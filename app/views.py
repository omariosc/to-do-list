from flask import render_template, flash
from app import app
from .forms import CreateAssessment
from app import db, models
import datetime

@app.route('/', methods=['GET', 'POST'])
def home():
	home={'description':'All Assessments'}
	return render_template('home.html',title='All Assessments',home=home)
@app.route('/create_assessment', methods=['GET', 'POST'])
def create():
	form = CreateAssessment()
	if form.validate_on_submit():
		flash('Successfully created assessment.')
		task = models.Assessment(title=form.title.data,code=form.code.data,deadline=form.deadline.data,description=form.description.data)
		db.session.add(task)
		db.session.commit() 
	return render_template('create.html',title='Create Assessments',form=form)
@app.route('/complete_assessment', methods=['GET', 'POST'])
def complete():
	complete={'description':'Completed Assessments'}
	return render_template('complete.html',title='Completed Assessments',complete=complete)
@app.route('/uncomplete_assessment', methods=['GET', 'POST'])
def uncomplete():
	uncomplete={'description':'Uncompleted Assessments'}
	return render_template('uncomplete.html',title='Uncompleted Asessments',uncomplete=uncomplete)
