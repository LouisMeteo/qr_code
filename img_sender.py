import requests

# URL du serveur Flask
url = 'http://localhost:5000/upload'

# Chemin d'accès à l'image que vous souhaitez envoyer
image_path = '/chemin/vers/votre/image.jpg'

# Ouverture du fichier image en mode binaire
with open(image_path, 'rb') as image_file:
    # Création de la payload de la requête avec le fichier image
    files = {'image': image_file}

    # Envoi de la requête POST avec la payload contenant l'image
    response = requests.post(url, files=files)

# Vérification du code de statut de la réponse
if response.status_code == 200:
    print('Image envoyée avec succès !')
else:
    print('Échec de l\'envoi de l\'image.')
