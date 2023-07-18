from flask import Flask, request, render_template, send_from_directory
import pyqrcode
import os

app = Flask(__name__)

# Chemin d'accès pour enregistrer les images
UPLOAD_FOLDER = 'C:/Users/C8OLH1/OneDrive - PHOENIX CONTACT GmbH & Co. KG/Bureau/codeppy/qr_code/upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Page d'accueil pour télécharger l'image
@app.route('/')
def home():
    return render_template('upload.html')

# Route pour traiter le téléchargement de l'image et générer le QR code
@app.route('/upload', methods=['POST'])
def upload():
    # Vérifier si un fichier a été téléchargé
    if 'image' not in request.files:
        return 'Aucun fichier téléchargé.'

    image = request.files['image']

    # Vérifier si le fichier a un nom
    if image.filename == '':
        return 'Nom de fichier vide.'

    # Enregistrer l'image sur le serveur
    image.save(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))

    # Générer l'URL de l'image
    image_url = request.host_url + 'image/' + image.filename

    # Générer le QR code contenant l'URL de l'image
    qr_code = pyqrcode.create(image_url)
    qr_filename = f"qr_{image.filename}.png"
    qr_code.png(os.path.join(app.config['UPLOAD_FOLDER'], qr_filename), scale=6)

    # Retourner l'URL de l'image et du QR code
    return f"Image : <img src='{image_url}'><br>QR Code : <img src='/image/{qr_filename}'>"

# Route pour accéder aux images
@app.route('/image/<filename>')
def get_image(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename.lower())

if __name__ == '__main__':
    app.run()
