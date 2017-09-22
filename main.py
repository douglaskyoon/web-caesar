from flask import Flask, request
from caesar import rotate_character, encrypt

app = Flask(__name__)
app.config['DEBUG'] = True

form= '''
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        
            <form action="/encrypt" method="post">
            <label for="rot">Rotate by:</label>
            <input type="text" name="rot" id="rot" value = "0"/>
            <br>
            <textarea type="text" name="text" id="text">{0}</textarea>
            <br>
            <input type="submit" value="Submit Query"/>
            </form>

    </body>
</html>
'''



@app.route("/encrypt", methods=['POST'])
def encrypted():
    txt = request.form['text']
    rotate = request.form['rot']
    txt_str = str(txt)
    rot_int = int(rotate)
    encrypt_txt = encrypt(txt_str, rot_int)
    content =  encrypt_txt 
    

    return form.format(content)

@app.route("/")
def index():
    return form.format('')



app.run()