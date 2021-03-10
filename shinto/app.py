from flask import Flask, request, render_template, render_template_string, send_from_directory
import os

app = Flask(__name__, static_folder='static', static_url_path='')
app.config['FLAG'] = os.environ.get('FLAG')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/robots.txt')
@app.route('/source-code.txt')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

@app.route('/tell-me-what-you-are-looking-for')
def searchfunction():
    search = request.args.get('search') or None
    if search != None:        
        def validation(s):
            blacklist = ['config', 'self']
            return ''.join(['{{% set {}=None%}}'.format(c) for c in blacklist])+s
        searchTerm = render_template_string(validation(search))
        return render_template('search.html', search=searchTerm)
    else:
        return render_template('search.html')

if __name__ == '__main__':
    app.run(debug=True)