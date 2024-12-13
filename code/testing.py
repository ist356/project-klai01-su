from PIL import Image
import os
'''
profile_icon_id = "300"

PROFILE_ICON_PATH = "../project-klai01-su/data/dragontail-14.24.1/14.21.1/img/profileicon/"
profile_icon_path = os.path.join(PROFILE_ICON_PATH, f"{profile_icon_id}.png")
print(profile_icon_path)
image = Image.open(f'{profile_icon_path}')
image.show()
'''
iconid = "6637"
# Define the path to the image (adjust the path for Mac)
image_path = f'../project-klai01-su/data/dragontail-14.24.1/14.24.1/img/profileicon/{iconid}.png'

image = Image.open(image_path)

image.show()