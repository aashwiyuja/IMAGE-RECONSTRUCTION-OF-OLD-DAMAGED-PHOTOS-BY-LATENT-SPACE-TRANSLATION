import os
from PIL import Image
import pandas as pd

# Set the path to the Flickr Face dataset
dataset_path = '/documention/masters_project/flickr-face-dataset/'

# Create a list to store the metadata information
metadata = []

# Iterate through the dataset directory and read each image
for root, _, files in os.walk(dataset_path):
    for file in files:
        if file.endswith('.jpg'):
            # Read the image using Pillow
            img_path = os.path.join(root, file)
            img = Image.open(img_path)

            # Extract the metadata from the filename
            _, _, gender, _, _, age, _ = file.split('_')
            age = int(age)

            # Add the metadata to the list
            metadata.append({
                'image_path': img_path,
                'gender': gender,
                'age': age
            })

# Convert the metadata list to a pandas dataframe
df = pd.DataFrame(metadata)

# Print the first 10 rows of the dataframe
print(df.head(10))
