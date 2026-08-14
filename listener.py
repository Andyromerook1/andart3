import json
from logger import raw_data, error

async def listen_passive(websocket):
    raw_data("Modo espejo activado. Escuchando mensajes...")
    try:
        async for message in websocket:
            try:
                parsed = json.loads(message)
                raw_data(f"JSON Recibido: {json.dumps(parsed, indent=2)}")
            except json.JSONDecodeError:
                raw_data(f"Mensaje Raw: {message}")
    except Exception as e:
        error(f"Error en escucha: {e}")