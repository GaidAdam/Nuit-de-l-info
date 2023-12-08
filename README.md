# Nuit-de-l-info
# Image and Video Compression Script

This Python script allows you to compress images and videos from a given URL, save them locally, and optionally upload them to Google Cloud Storage.

## Usage

1. **Install Dependencies**

   Before running the script, make sure to install the required dependencies:

   ```bash
   pip install opencv-python Pillow requests
Run the Script

bash
Copy code
python compress_and_upload.py
Follow the Prompts

Enter the desired size or bitrate.
Enter a new file name.
Enter the file URL.
Enter the output directory (must already exist).
Output

The compressed file will be saved locally, and the script will print the local path to the compressed file.

Uncomment the relevant lines in the script if you want to upload the compressed file to Google Cloud Storage.

Note: This script supports image formats (JPEG, PNG, GIF) and video formats (MP4, AVI, MOV). Adjust dimensions and settings as needed.