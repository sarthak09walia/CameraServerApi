from flask import Flask, jsonify
import psutil

app = Flask(__name__)


@app.route("/")
def system_status():
    cpu_percent = psutil.cpu_percent(interval=1)
    ram_info = psutil.virtual_memory().percent
    rom_info = psutil.disk_usage('/').percent
    return jsonify({'status': 'online', 'cpu': cpu_percent, 'ram': f"{ram_info}%", 'rom': f"{rom_info}%"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
