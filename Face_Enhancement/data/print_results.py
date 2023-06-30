import os
from PIL import Image
# Set the directory where the images are located
image_dir = '/documents/masters_project/test_results/images'
# Loop through each file in the directory
for filename in os.listdir(image_dir):
    # Check if the file is an image
    if images.endswith('.jpg') or images.endswith('.png'):
        
        # Load the image using Pillow
        img_path = os.path.join(image_dir, images)
        img = Image.open(img_path)

        # Save the modified image
        modified_img_path = os.path.join(image_dir, 'modified_' + images)
        img.save(modified_img_path)
# Load the original image
img_path = '/documents/masters_project/test_results/images/image.jpg'
img = Image.open(img_path)
# Convert the image to RGB mode
rgb_img = img.convert('RGB')
# Define a function to improvise the colors using RGB mode
def improvise_rgb(pixel):
    r, g, b = pixel
    return (r + 50, g - 25, b + 75)
    
# Apply the function to each pixel in the image
improvised_rgb_img = rgb_img.point(improvise_rgb)

# Convert the improvised image to CMYK mode
improvised_cmyk_img = improvised_rgb_img.convert('CMYK')

# Save the improvised images
improvised_rgb_img_path = '/documents/masters_project/test_results/images/image.jpg/improvised_rgb_image.jpg'
improvised_rgb_img.save(improvised_rgb_img_path)
improvised_cmyk_img_path = '/documents/masters_project/test_results/images/image.jpg/improvised_cmyk_image.jpg'
improvised_cmyk_img.save(improvised_cmyk_img_path)

# Print the original and improvised images in CMYK modes

print('Improvised image in CMYK mode:')
print(f'    Mode: {improvised_cmyk_img.mode}')
print(f'    Size: {improvised_cmyk_img.size}')
