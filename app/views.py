from flask import render_template, flash
from app import app
from .forms import CreateAssessment
from app import db, models
import datetime

@app.route('/', methods=['GET', 'POST'])
def home():
	description = 'You have no assessments.'
	tasks = models.Assessment.query.order_by(models.Assessment.id).all()
	if len(tasks) > 0 :
		description = ''
	for task in tasks:
		if task.status == 0:
			task.status = "Uncomplete"
		elif task.status == 1:
			task.status = "Completed"
	return render_template('home.html',title='All Assessments',description=description,tasks=tasks)
@app.route('/create_assessment', methods=['GET', 'POST'])
def create():
	form = CreateAssessment()
	if form.validate_on_submit():
		flash('Successfully created assessment.')
		task = models.Assessment(title=form.title.data,code=form.code.data,deadline=form.deadline.data,description=form.description.data, status=0)
		db.session.add(task)
		db.session.commit()
	return render_template('create.html',title='Create Assessments',form=form)
@app.route('/complete_assessment', methods=['GET', 'POST'])
def complete():
	description = 'You have not completed any assessments.'
	tasks = models.Assessment.query.filter_by(status=1).order_by(models.Assessment.id).all()
	if len(tasks) > 0 :
		description = ''
	for task in tasks:
		task.status = "Completed"
	return render_template('complete.html',title='Completed Assessments',description=description,tasks=tasks)
@app.route('/uncomplete_assessment', methods=['GET', 'POST'])
def uncomplete():
	description = 'Well Done! You have no uncompleted assessments.'
	tasks = models.Assessment.query.filter_by(status=0).order_by(models.Assessment.id).all()
	if len(tasks) > 0 :
		description = ''
	for task in tasks:
		task.status = "Uncomplete"
	return render_template('uncomplete.html',title='Uncompleted Asessments',description=description,tasks=tasks)
