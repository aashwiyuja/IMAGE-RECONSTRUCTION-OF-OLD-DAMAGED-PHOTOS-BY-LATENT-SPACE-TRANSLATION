from PIL import Image

# Load the original image
img_path = '/documents/masters_project/test_results/images/image.jpg'
img = Image.open(img_path)

# Define the scaling factor
scale_factor = 2

# Get the original size of the image
width, height = img.size

# Calculate the new size of the image
new_width = width * scale_factor
new_height = height * scale_factor

# Upsample the image using bilinear interpolation
upscaled_img = img.resize((new_width, new_height), resample=Image.BILINEAR)

# Save the upscaled image
upscaled_img_path = '/documents/masters_project/test_results/images/image.jpg'
upscaled_img.save(upscaled_img_path)
