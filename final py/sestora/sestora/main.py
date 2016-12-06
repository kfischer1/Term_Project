from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.htm")

@app.route('/contact_us.htm')
def ContactUs():
    return render_template("contact_us.htm")

@app.route('/store/<string:first>/<string:last>/<string:email>/<string:status>/<string:location>/<string:comments>', methods=['POST'])
def StoreForm(first, last, email, status, location, comments):
	info = [first, last, email, status, location, comments]
	file = open('contacts.csv', 'a')
	file.write(','.join(info) + '\n')
	file.close()
	return 'success'

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=8888,debug=True)
