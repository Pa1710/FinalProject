"""Route declaration."""
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def home():
    """Landing page."""
    nav = [
        {'name': 'Landing Page', 'url': 'https://example.com/1'},
        {'name': 'More Info', 'url': 'https://example.com/2'},
        {'name': 'Pictures', 'url': 'https://example.com/3'}
    ]
    return render_template(
        'home.html',
        nav=nav,
        title="Demo Website build in Jinga",
        description="Smarter page templates created with Flask and Jinga",
        status={'active': True}
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
