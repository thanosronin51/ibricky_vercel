# build_files.sh
pip install -r requirements.txt
import cloudinary
import cloudinary.uploader
import cloudinary.api
cloudinary.config( 
  cloud_name = "dwpqoubdw", 
  api_key = "746427962229227", 
  api_secret = "Mw778m_arBap_WKexphIdoar0dw" 
)

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


python3.9 manage.py collectstatic
python3.9 manage.py makemigrations
python3.9 manage.py migrate
