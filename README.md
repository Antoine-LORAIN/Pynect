# Pynect v0.1-Dev

## Installation
#### Installation de libfreenect

Il est nécessaire d'utiliser Raspberry Pi OS avec interface graphique d'installé.<br>
> [!CAUTION]
> L'utilisation d'une distribution linux avec une interace graphiqe est obligatoire. L'affichage des images ne se fera pas si vous n'avez pas d'interface.

> [!IMPORTANT]
> Les utilisations de Pynect sur une autre distribution linux que raspberry pi OS n'ont pas été testée. A vos risques et périls

> [!IMPORTANT]
> Il est nécessaire d'avoir les droits administrateurs pour l'installation.
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
Clonez le dépot github de [libfreenect](https://github.com/OpenKinect/libfreenect)
```
cd ~/
git clone https://github.com/OpenKinect/libfreenect.git
```
Lancez la compilation
```
cd libfreenect
mkdir build
cd build
cmake -L ..
make
sudo make install
sudo ldconfig /usr/local/lib64
```
> [!NOTE]
> Certaines erreur de compialtion peuvent apparaitre. Elles s'influencent pas le processus d'installation et l'utilisation de Pynect
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
![Vue en couleur et en profondeur de la kinect avec libfreenect](https://github.com/Antoine-LORAIN/Pynect/blob/835f096545ded82342348291a202f41c3b7e8203/images/freenect-glview.png)

#### Installation de freenect pour python
Installez les paquets suivant nécessaire à installaion de freenect
```
sudo apt install cython python-dev python-numpy
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
> Certaines erreur de compialtion peuvent apparaitre. Elles s'influencent pas le processus d'installation et l'utilisation de Pynect

Vous pouvez désormais clonez le dépôt Pynect
```
cd ~/
git clone {{{URL A INSERER UNE FOIS FINI}}}
```

## Utilisation
Pour utiliser Pynect, lancez le fichier ```main.py``` situé à la racine du dépôt
```
cd ~/Pynect
python main.py
```
> [!CAUTION]
> Si l'application met du temps à démarrer ou que vous avez ce message : 
> ```
>Message à ajouter
>```
>Initialisez la kinect avec
>```
>freenect-glview
>```
