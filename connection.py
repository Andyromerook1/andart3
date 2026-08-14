import ssl
import websockets
from logger import info, error

async def connect_ws(target_uri, headers):
    try:
        info(f"Conectando a {target_uri}...")
        ssl_context = ssl.create_default_context()
        connection = await websockets.connect(
            target_uri,
            extra_headers=headers,
            ssl=ssl_context,
            ping_interval=20,
            ping_timeout=60
        )
        success("Conexión WebSocket establecida correctamente.")
        return connection
    except Exception as e:
        error(f"Fallo en la conexión: {e}")
        return None