from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/about')
def about_me():
    return render_template('about.html')

@app.route('/components')
def components():
    return render_template('components.html')

@app.route('/contact')
def contacts():
    return render_template('contact.html')

@app.route('/work.html')
def work():
    return render_template('work.html')

@app.route('/works')
def works():
    return render_template('works.html')

@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

# Writes contact information submitted on site to file
def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email}, {subject}, {message}')

# Captures data submitted in form
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        return redirect(url_for('thank_you'))
    else:
        return 'something went wrong'






if __name__ == '__main__':
  app.run(host='0.0.0.0', port=30006, debug=True)