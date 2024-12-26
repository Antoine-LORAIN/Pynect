import ctypes
import numpy as np
import cv2
import clr  # Nécessaire pour charger une bibliothèque .NET

# Charger le SDK Kinect v1.8
clr.AddReference(r"C:\Program Files\Microsoft SDKs\Kinect\v1.8\Assemblies\Microsoft.Kinect.dll")

# Importer les classes du SDK Kinect v1.8
from Microsoft.Kinect import KinectSensor, ColorImageFormat, DepthImageFormat

# Initialisation Kinect
sensor = KinectSensor.KinectSensors[0]  # Utiliser le premier capteur détecté
if not sensor:
    print("Aucune Kinect détectée")
    exit()

# Démarrer le capteur
sensor.Start()

# Activer le flux couleur
sensor.ColorStream.Enable(ColorImageFormat.RgbResolution640x480Fps30)

# Activer le flux de profondeur
sensor.DepthStream.Enable(DepthImageFormat.Resolution640x480Fps30)

# Fonction pour capturer une image couleur
def capture_color_image():
    frame = sensor.ColorStream.OpenNextFrame(1000)  # Timeout de 1000ms
    if frame:
        # Obtenir les données d'image brute
        pixel_data = np.frombuffer(frame.GetRawPixelData(), dtype=np.uint8)
        # Reshape en une image 640x480 avec 4 canaux (BGRA)
        image = pixel_data.reshape((frame.Height, frame.Width, 4))[:, :, :3]  # Supprime le canal alpha
        return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convertir en RGB
    return None

# Fonction pour capturer une image de profondeur
def capture_depth_image():
    frame = sensor.DepthStream.OpenNextFrame(1000)  # Timeout de 1000ms
    if frame:
        # Créer un tableau NumPy pour recevoir les données de profondeur
        depth_data = np.empty(frame.PixelDataLength, dtype=np.uint16)
        # Copier les données de profondeur dans le tableau
        frame.CopyDepthImagePixelDataTo(depth_data)
        # Reshape en une image 640x480
        depth_image = depth_data.reshape((frame.Height, frame.Width))
        # Normaliser pour l'affichage
        depth_image = (depth_image / depth_image.max() * 255).astype(np.uint8)
        return depth_image
    return None



# Affichage en temps réel
def main():
    while True:
        color_image = capture_color_image()
        depth_image = capture_depth_image()

        if color_image is not None:
            cv2.imshow("Image Kinect - Couleur", color_image)
        else:
            print("Erreur lors de la capture de l'image couleur.")

        if depth_image is not None:
            cv2.imshow("Image Kinect - Profondeur", depth_image)
        else:
            print("Erreur lors de la capture de l'image de profondeur.")

        # Sortir de la boucle si l'utilisateur appuie sur la touche 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Fermer les fenêtres et arrêter le capteur
    cv2.destroyAllWindows()
    sensor.Stop()

if __name__ == "__main__":
    main()
