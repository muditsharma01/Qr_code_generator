from flask import Flask, render_template, request, send_file
import qrcode as qr
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    url = request.form['url']
    img = qr.make(url)
    filename = "qr_code.png"
    img.save(os.path.join(app.static_folder, filename))
    return render_template('show_qr.html', qr_image=filename)

if __name__ == '__main__':
    app.run(debug=True)
