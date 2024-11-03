from flask import Flask, request, jsonify
import socket

app = Flask(__name__)

@app.route('/get-ip', methods=['GET'])
def get_ip():
    ip_address = request.remote_addr
    return jsonify({'ip': ip_address})


# function getPublicIP() {
#   fetch('https://api.ipify.org?format=json')
#     .then(response => response.json())
#     .then(data => {
#       console.log('Tu dirección IP pública es: ', data.ip);
#     })
#     .catch(error => console.error('Error al obtener la IP pública:', error));
# }

# getPublicIP();



# https://api.ipify.org/?format=json

@app.route('/get-public-ip', methods=['GET'])
def get_public_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  
        public_ip = s.getsockname()[0]
        s.close()
        return jsonify({"public_ip": public_ip}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
