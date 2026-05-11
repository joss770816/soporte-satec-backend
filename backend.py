from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({
        "service": "Earby API - Soporte SATEC",
        "status": "activo",
        "endpoints": {
            "/chat": "POST - Envía mensajes",
            "/health": "GET - Verifica estado"
        }
    })

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    
    if not data or 'mensaje' not in data:
        return jsonify({"error": "Falta el campo 'mensaje'"}), 400
    
    mensaje = data['mensaje'].lower()
    
    if "gps" in mensaje:
        respuesta = "🔧 El GPS tarda hasta 3 minutos en fijar señal. ¿Has verificado que estás en un área abierta?"
    elif "contraseña" in mensaje or "password" in mensaje:
        respuesta = "🔐 Puedes restablecer tu contraseña en la sección 'Olvidé mi contraseña' del panel."
    else:
        respuesta = "📡 He registrado tu consulta. ¿Podrías darme más detalles? (Escribe 'soporte humano' para hablar con una persona)"
    
    return jsonify({
        "respuesta": respuesta,
        "status": "success"
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
