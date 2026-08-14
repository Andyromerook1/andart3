import asyncio
import json
from logger import success, error, info

async def fire_twins(websocket, original_message, times=2, alter_func=None):
    # SEGURIDAD: Límite estricto para evitar DoS
    if times > 5:
        error("Límite de seguridad: No se pueden enviar más de 5 paquetes en ráfaga.")
        times = 5

    info(f"Preparando ráfaga de {times} paquetes...")
    
    payloads = []
    for i in range(times):
        if alter_func and i > 0:
            modified = alter_func(original_message)
            payloads.append(modified)
        else:
            payloads.append(original_message)

    tasks = [websocket.send(p) for p in payloads]
    
    try:
        await asyncio.gather(*tasks)
        success(f"Ráfaga de {times} paquetes inyectada en el servidor.")
    except Exception as e:
        error(f"Error al inyectar la ráfaga: {e}")