#!/usr/bin/env python3
import connexion
from flask import render_template

# Create the application instance
app = connexion.App(__name__, specification_dir='./')

# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yaml', arguments={'title': 'Navigator Sharing Data'}, pythonic_params=True)

# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:8080/
    :return:        the rendered template 'index.html'
    """
    
    return render_template('index.html')   

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)