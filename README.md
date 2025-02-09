# Pynect v1

## Installation
#### Installation de libfreenect

Il est nécessaire d'utiliser Raspberry Pi OS avec interface graphique.<br>
> [!CAUTION]
> L'utilisation d'une distribution linux avec une interace graphiqe est obligatoire. L'affichage des images ne se fera pas si vous n'avez pas d'interface.

> [!IMPORTANT]
> Les utilisations de Pynect sur d'autres distributions linux que raspberry pi OS n'ont pas été testées. A vos risques et périls

> [!IMPORTANT]
> Il est nécessaire d'avoir les droits administrateurs pour l'installation.

Mettez à jour le raspberry pi avec :
```
sudo apt update
sudo apt upgrade -y
```
Installer les dépendances nécessaire pour la compilation de libfreenect :
```
sudo apt install git cmake freeglut3-dev pkg-config build-essential libxmu-dev libxi-dev libusb-1.0-0-dev -y
```
Clonez le dépot github de [libfreenect](https://github.com/OpenKinect/libfreenect)
```
cd ~/
git clone https://github.com/OpenKinect/libfreenect.git
```
Compilez libfreenect
```
cd ~/libfreenect
mkdir build
cd build
cmake -L ..
make
sudo make install
sudo ldconfig /usr/local/lib64
```
> [!NOTE]
> Certaines erreurs de compialtion peuvent apparaitre. Elles s'influencent pas le processus d'installation ainsi l'utilisation de Pynect

Afin de pouvoir executer libfreenect (et Pynect) dans les droits administrateur, executez les commandes suivantes
```
sudo adduser $USER video
sudo adduser $USER plugdev
```
Il faut créer un fichier de règles pour la kinect <br>
Éditez le fichier suivant
```
sudo nano /etc/udev/rules.d/51-kinect.rules
```
et ajoutez les lignes suivantes
```
# ATTR{product}=="Xbox NUI Motor"
SUBSYSTEM=="usb", ATTR{idVendor}=="045e", ATTR{idProduct}=="02b0", MODE="0666"
# ATTR{product}=="Xbox NUI Audio"
SUBSYSTEM=="usb", ATTR{idVendor}=="045e", ATTR{idProduct}=="02ad", MODE="0666"
# ATTR{product}=="Xbox NUI Camera"
SUBSYSTEM=="usb", ATTR{idVendor}=="045e", ATTR{idProduct}=="02ae", MODE="0666"
# ATTR{product}=="Xbox NUI Motor"
SUBSYSTEM=="usb", ATTR{idVendor}=="045e", ATTR{idProduct}=="02c2", MODE="0666"
# ATTR{product}=="Xbox NUI Motor"
SUBSYSTEM=="usb", ATTR{idVendor}=="045e", ATTR{idProduct}=="02be", MODE="0666"
# ATTR{product}=="Xbox NUI Motor"
SUBSYSTEM=="usb", ATTR{idVendor}=="045e", ATTR{idProduct}=="02bf", MODE="0666"
```
Redémarrez le raspberry
```
reboot 
```
Testez l'installation de libfreenect
```
freenect-glview
```
#### Installation de freenect pour python
Installez les paquets suivants qui sont nécessaire à l'installaion et à l'utilisation de freenect
```
sudo apt install cython3 python3-dev python3-numpy python3-opencv
```
Déplacez vous dans le dossier freenect
```
cd ~/libfreenect/wrappers/python
```
Préparez l'installation du wrapper
```
sudo python setup.py build_ext -f
```
Installez le wrapper python
```
sudo python setup.py install
```
> [!NOTE]
> Certaines erreurs de compialtion peuvent apparaitre. Elles s'influencent pas le processus d'installation ainsi que l'utilisation de Pynect

Vous pouvez désormais clonez le dépôt Pynect
```
cd ~/
git clone https://github.com/Antoine-LORAIN/Pynect.git
```

## Utilisation
Pour utiliser Pynect, lancez le fichier ```main.py``` situé à la racine du dépôt
```
cd ~/Pynect
python main.py
```
> [!CAUTION]
> Si l'application ne ce lance pas et que ```Ctrl+C``` ne fait rien, fermez le terminal et executez
> ```freenect-glview```
> Fermez cette fenêtre en appuiant sur ```Echap``` et relancez l'application
