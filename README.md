# Pynect v0.1-Dev

## Installation

Il est nécessaire d'utiliser un raspberry pi avec Raspberry Pi OS avec interface graphique d'installé.<br>
Mettez à jour le raspberry pi avec :
```
sudo apt update
sudo apt upgrade -y
```
Installer les dépendances nécessaire pour la compilation de libfreenect :
```
sudo apt install git cmake freeglut3-dev \ 
pkg-config build-essential libxmu-dev \
libxi-dev libusb-1.0-0-dev -y
```
Clonez le dépot github de [libfreenect]("https://github.com/OpenKinect/libfreenect")
