# Remove_duplicate_images
This Python script identifies and removes duplicate images in a specified folder. It uses image hashing to efficiently detect duplicates and can optionally delete the identified duplicates.

## Features

- **Image Hashing**: Uses the `dhash` or `phash` to generate unique hashes for each image in the specified folder.
- **Duplicate Detection**: Compares the generated hashes to identify duplicate images.
- **Optional Deletion**: Optionally deletes the detected duplicate images from the folder.
- **JSON Result File**: Optionally saves the result of duplicates in a JSON file for verification before deletion.

## Usage (steps by steps)
## Step 1:
Clone this repository using this
```sh
git clone git@github.com:AleDuarte20/Remove_duplicate_images.git
```

## Step 2:
Open your terminal
```sh
cd /project/Remove_duplicate_images
```
## Step 3:
Create venv for your project
```sh
python -m venv venv
```
In Windows
```sh
.\venv\Scripts\activate
```
Linux or macOs
```sh
source venv/bin/activate
```
## Step 4:
After activate your venv install all dependencies
```sh
pip install -r requirements.txt
```
## Step 5:
Change `images_folder_path` before execute app.py
### Example
`images_folder_path = os.path.join("/home","user_example","images_folder")`
## Step 6:
Execute `app.py`
```sh
python app.py
```
### Example Output
```sh
Files length: 4
workers: 8
creating hash for all images
get duplicates
duplicates: [{'name': 'image1.jpg', 'duplicates': ['image2.jpg', 'image3.jpg']}]
duplicates length: 1
remove duplicates from folder
duplicate image: /path/to/your/images/folder/image2.jpg
removed successfully
duplicate image: /path/to/your/images/folder/image3.jpg
removed successfully
proccess duration: 0:00:00.267355
```
## Contributing
It is one of my first projects in python, any help, contributions or advice would be welcome. 
