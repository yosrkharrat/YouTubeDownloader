from flask import Flask, request, send_file, render_template
import yt_dlp
import os
app = Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html"


@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s'
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
    except Exception as e:
        return f"Error during download: {e}"

    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
