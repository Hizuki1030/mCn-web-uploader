from flask import Flask
app = Flask(__name__, static_folder='.', static_url_path='')
@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/LatestFirmwareUploader')
def page1():
    # 変数展開(messageとnameの値がHTMLに渡される)
    return app.send_static_file('LatestFirmwareUploader.html')


app.run(port=8000, debug=True)