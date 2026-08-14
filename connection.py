import ssl
import websockets
from logger import info, error, success

async def connect_ws(target_uri, headers):
    try:
        # Falsificar User-Agent si no viene en headers
        if "User-Agent" not in headers:
            headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
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
