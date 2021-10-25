from flask import render_template
from app import app

@app.route('/', methods=['GET', 'POST'])
def home():
	home={'description':'All Assessments'}
	return render_template('home.html',title='All',home=home)
@app.route('/create_assessment', methods=['GET', 'POST'])
def create():
    create={'description':'Create Assessment'}
    return render_template('create.html',title='Create',create=create)
@app.route('/complete_assessment', methods=['GET', 'POST'])
def complete():
	complete={'description':'Completed Assessments'}
	return render_template('complete.html',title='Completed',complete=complete)
@app.route('/uncomplete_assessment', methods=['GET', 'POST'])
def uncomplete():
	uncomplete={'description':'Uncompleted Assessments'}
	return render_template('uncomplete.html',title='Uncompleted',uncomplete=uncomplete)
