#!/usr/bin/env python3
import asyncio
import argparse
import json
import sys
from connection import connect_ws
from listener import listen_passive
from injector import fire_twins
from logger import info, error, success

async def main():
    parser = argparse.ArgumentParser(description="WSS Race Scalpel - Bisturí para WebSockets en Termux")
    parser.add_argument("--listen", action="store_true", help="Modo espejo: solo escucha el tráfico")
    parser.add_argument("--inject", type=int, help="Modo ataque: duplica el mensaje N veces (max 5)")
    parser.add_argument("--payload", type=str, help='Payload personalizado en formato JSON (ej: \'{"id":1}\')')
    parser.add_argument("--config", type=str, default="config.json", help="Archivo de configuración")
    
    args = parser.parse_args()

    # Cargar config
    try:
        with open(args.config, 'r') as f:
            config = json.load(f)
    except FileNotFoundError:
        error("Archivo config.json no encontrado. Usa el template.")
        sys.exit(1)

    target = config.get("target_ws")
    headers = config.get("headers", {})
    max_burst = min(config.get("max_burst", 3), 5)

    ws = await connect_ws(target, headers)
    if not ws:
        return

    try:
        if args.listen:
            await listen_passive(ws)
        elif args.inject:
            if not args.payload:
                info("No se especificó --payload. Usando mensaje de prueba estándar.")
                payload = '{"test": "race_condition"}'
            else:
                payload = args.payload

            # Función de alteración (ejemplo: modifica el campo "count" o "value")
            def alter_example(original):
                try:
                    data = json.loads(original)
                    if "count" in data:
                        data["count"] += 1000
                    elif "value" in data:
                        data["value"] = "hacked"
                    else:
                        data["modified"] = True
                        data["timestamp"] = "2026"
                    return json.dumps(data)
                except:
                    return original + " (modified)"

            times = min(args.inject, max_burst, 5)
            await fire_twins(ws, payload, times, alter_example)
            await asyncio.sleep(2)
        else:
            parser.print_help()
    except KeyboardInterrupt:
        info("Cerrando conexión por petición del usuario...")
    finally:
        await ws.close()
        info("Conexión cerrada.")

if __name__ == "__main__":
    asyncio.run(main())