'''
Main file for the Comprehensive Job Alerts System (CJAS) web application.
'''
from flask import Flask, render_template, request
from job_search import JobSearch
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        keywords = request.form.get('keywords')
        location = request.form.get('location')
        job_search = JobSearch()
        job_results = job_search.search_jobs(keywords, location)
        return render_template('results.html', results=job_results)
    return render_template('search.html')
if __name__ == '__main__':
    app.run(debug=True)