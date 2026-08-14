#!/data/data/com.termux/files/usr/bin/bash

# Colores para la terminal
GREEN='\033[0;32m'
CYAN='\033[0;36m'
RED='\033[0;31m'
NC='\033[0m' # Sin Color

echo -e "${CYAN}======================================${NC}"
echo -e "${CYAN}  WSS-Race-Scalpel - Instalador     ${NC}"
echo -e "${CYAN}======================================${NC}"

echo -e "${GREEN}[1/5] Actualizando repositorios de Termux...${NC}"
pkg update -y && pkg upgrade -y

echo -e "${GREEN}[2/5] Instalando herramientas esenciales (Python, Rust, binutils, Git)...${NC}"
pkg install python rust binutils git -y

echo -e "${GREEN}[3/5] Instalando certificados SSL para evitar errores de conexión...${NC}"
pkg install ca-certificates -y

echo -e "${GREEN}[4/5] Actualizando pip e instalando dependencias de Python...${NC}"
pip install --upgrade pip
pip install -r requirements.txt

echo -e "${GREEN}[5/5] Dando permisos de ejecución al script principal...${NC}"
chmod +x main.py

echo -e "${CYAN}======================================${NC}"
echo -e "${GREEN}✅ Instalación completada con éxito.${NC}"
echo -e "${CYAN}Para probar el modo escucha:${NC} python main.py --listen"
echo -e "${CYAN}Para probar el ataque:${NC} python main.py --inject 3 --payload '{\"test\":\"hola\"}'"
echo -e "${CYAN}======================================${NC}"
