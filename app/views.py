from flask import render_template, flash, request
from app import app
from .forms import CreateAssessment
from app import db, models

home_description = 'You have no assessments.'
home_template = 'home.html'
home_title = 'All Assessments'
comp_description = 'You have not completed any assessments.'
completed_title = 'Completed Assessments'
uncomp_description = 'Well Done! You have no uncompleted assessments.'
uncomplete_title = 'Uncompleted Assessments'

def flash_unmark():
	flash('Successfully unmarked assessment.')
def flash_mark():
	flash('Successfully marked assessment as complete.')

@app.route('/', methods=['GET', 'POST'])
def home():
	description = home_description
	tasks = models.Assessment.query.order_by(models.Assessment.id).all()
	if len(tasks) > 0 :
		description = ''
	return render_template(home_template,title=home_title,description=description,tasks=tasks)
@app.route('/mark/<task_id>', methods=['GET', 'POST'])
def mark(task_id):
	description = home_description
	models.Assessment.query.filter_by(id=task_id).update({"status": 1})
	db.session.commit()
	tasks = models.Assessment.query.order_by(models.Assessment.id).all()
	if len(tasks) > 0 :
		description = ''
	flash_mark()
	return render_template(home_template,title=home_title,description=description,tasks=tasks)
@app.route('/unmark/<task_id>', methods=['GET', 'POST'])
def unmark(task_id):
	description = home_description
	models.Assessment.query.filter_by(id=task_id).update({"status": 0})
	db.session.commit()
	tasks = models.Assessment.query.order_by(models.Assessment.id).all()
	if len(tasks) > 0 :
		description = ''
	flash_unmark()
	return render_template(home_template,title=home_title,description=description,tasks=tasks)
@app.route('/delete/<task_id>', methods=['GET', 'POST'])
def delete(task_id):
	description = home_description
	task = models.Assessment.query.filter_by(id=task_id).one()
	db.session.delete(task)
	db.session.commit()
	tasks = models.Assessment.query.order_by(models.Assessment.id).all()
	if len(tasks) > 0 :
		description = ''
	flash_mark()
	return render_template(home_template,title=home_title,description=description,tasks=tasks)
@app.route('/create', methods=['GET', 'POST'])
def create():
	form = CreateAssessment()
	if form.validate_on_submit():
		task = models.Assessment(title=form.title.data,code=form.code.data,deadline=form.deadline.data,description=form.description.data, status=0)
		db.session.add(task)
		db.session.commit()
		flash('Successfully created assessment.')
	return render_template('create.html',title='Create Assessments',form=form,task=0)
@app.route('/complete', methods=['GET', 'POST'])
def complete():
	completed_description = comp_description
	tasks = models.Assessment.query.filter_by(status=1).order_by(models.Assessment.id).all()
	if len(tasks) > 0 :
		completed_description = ''
	return render_template(home_template,title=completed_title,description=completed_description,tasks=tasks)
@app.route('/complete/unmark/<task_id>', methods=['GET', 'POST'])
def unmark_completed(task_id):
	completed_description = comp_description
	models.Assessment.query.filter_by(id=task_id).update({"status": 0})
	db.session.commit()
	tasks = models.Assessment.query.filter_by(status=1).order_by(models.Assessment.id).all()
	if len(tasks) > 0 :
		completed_description = ''
	flash_unmark()
	return render_template(home_template,title=completed_title,description=completed_description,tasks=tasks)
@app.route('/complete/delete/<task_id>', methods=['GET', 'POST'])
def delete_completed(task_id):
	completed_description = comp_description
	task = models.Assessment.query.filter_by(id=task_id).one()
	db.session.delete(task)
	db.session.commit()
	tasks = models.Assessment.query.filter_by(status=1).order_by(models.Assessment.id).all()
	if len(tasks) > 0 :
		completed_description = ''
	flash_unmark()
	return render_template(home_template,title=completed_title,description=completed_description,tasks=tasks)
@app.route('/uncomplete', methods=['GET', 'POST'])
def uncomplete():
	uncomplete_description = uncomp_description
	tasks = models.Assessment.query.filter_by(status=0).order_by(models.Assessment.id).all()
	if len(tasks) > 0 :
		uncomplete_description = ''
	return render_template(home_template,title=uncomplete_title,description=uncomplete_description,tasks=tasks)
@app.route('/uncomplete/mark/<task_id>', methods=['GET', 'POST'])
def mark_complete(task_id):
	uncomplete_description = uncomp_description
	models.Assessment.query.filter_by(id=task_id).update({"status": 1})
	db.session.commit()
	tasks = models.Assessment.query.filter_by(status=0).order_by(models.Assessment.id).all()
	if len(tasks) > 0 :
		uncomplete_description = ''
	flash_mark()
	return render_template(home_template,title=uncomplete_title,description=uncomplete_description,tasks=tasks)
@app.route('/uncomplete/delete/<task_id>', methods=['GET', 'POST'])
def delete_uncomplete(task_id):
	uncomplete_description = uncomp_description
	task = models.Assessment.query.filter_by(id=task_id).one()
	db.session.delete(task)
	db.session.commit()
	tasks = models.Assessment.query.filter_by(status=0).order_by(models.Assessment.id).all()
	if len(tasks) > 0 :
		uncomplete_description = ''
	flash_mark()
	return render_template(home_template,title=uncomplete_title,description=uncomplete_description,tasks=tasks)
@app.route('/edit/<task_id>', methods=['GET', 'POST'])
def edit(task_id):
	task = models.Assessment.query.filter_by(id=task_id).one()
	form = CreateAssessment()
	if form.validate_on_submit():
		task.title=form.title.data
		task.code=form.code.data
		task.deadline=form.deadline.data
		task.description=form.description.data
		db.session.commit()
		flash('Successfully edited assessment.')
	return render_template('create.html',title='Edit Assessment',form=form,task=task)
