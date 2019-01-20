from flask import Flask
from flask import request
from flask import render_template_string

app = Flask(__name__)

@app.errorhandler(404)
def hello(e):
    template = '''
    {%% block body %%}
        <div class="center-content error">
            <h1>Oops! That page doesn't exist.</h1>
            <h3>%s</h3>
        </div>
    {%% endblock %%}
    ''' % (request.url)
    return render_template_string(template), 404

if __name__ == '__main__':
    app.run(port=5000)