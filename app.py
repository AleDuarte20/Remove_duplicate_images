from PIL import Image
import imagehash
import os
import json
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

# Path to the images folder
images_folder_path = os.path.join("/home","user_example","images_folder")

# Lists to store image hashes and duplicates results
hash_list = []
duplicates_result = []


def create_image_hash(image):
    # Create a hash of the image and add it to the hash list (only images)

    if not image.endswith(".mp4"):

        try:
            img = Image.open(os.path.join(images_folder_path, image))

            image_hash = str(imagehash.dhash(img, hash_size=8)) # dhash is faster and sufficiently accurate
            # image_hash = str(imagehash.phash(img, hash_size=8)) # phash is slower but very accurate

            hash_list.append({"name":image, "hash": image_hash})

        except Exception as e:
            print(f"Error processing image {image}: {e}")


def find_duplicates(image):
    # Find duplicate images in the hash list

    global hash_list

    original_image = list(filter(lambda x: x["name"] == image["name"], hash_list))

    if len(original_image) > 0:

        duplicate_images = list(filter(lambda x: x["name"] != image["name"] and x["hash"] == image["hash"], hash_list))
        duplicate_images = [image["name"] for image in duplicate_images]
        # print(f"duplicates: {duplicate_images}")
        
        if len(duplicate_images) > 0:
            
            hash_list = list(filter(lambda x: x["name"] not in duplicate_images, hash_list))

            duplicates_result.append({"name": image["name"], "duplicates": duplicate_images})

def save_duplicates_result(save_result):
    # Create a JSON file at the root to verify the images

    json_path = os.path.join(os.path.abspath(path="./"), "result.json")
    file_content = json_str = json.dumps(duplicates_result, indent=4)

    if save_result:
        with open(json_path, "w") as file:
            file.write(file_content)
        print("File created")


def remove_duplicates(image):
    # Delete duplicate files from the folder

    for image in image["duplicates"]:

        duplicate_image_path = os.path.join(images_folder_path, image)
        print(f"duplicate image: {duplicate_image_path}")

        if os.path.exists(duplicate_image_path):

            os.remove(duplicate_image_path)
            print(f"removed successfully")
        
        else:
            print("Cannot remove image")



def main(workers_number, save_result, delete_duplicate=False):
    # Main function that executes hashing, duplicate finding, save results, and deletion duplicates

    print(f"workers: {workers_number}")
    
    with ThreadPoolExecutor(max_workers=workers_number) as executor:
        print(f"creating hash for all images")
        list(executor.map(create_image_hash, images))

        print(f"get duplicates")
        list(executor.map(find_duplicates, hash_list))
        print(f"duplicates: {duplicates_result}\nduplicates length: {len(duplicates_result)}")

        save_duplicates_result(save_result)

        if delete_duplicate and len(duplicates_result) > 0:
            print(f"remove duplicates from folder")
            list(executor.map(remove_duplicates, duplicates_result))


if __name__ == "__main__":

    # List images in the specified folder
    images = os.listdir(images_folder_path)
    print(f"Files length: {len(images)}")

    # Choose the number of workers (threads)
    workers_number = os.cpu_count() # Use the number of CPUs on your PC
    save_result = True # Save the result in a JSON file, recommended to check before deleting duplicates
    delete_duplicate = False # Change to True if you want to delete duplicates

    start_time = datetime.now()
    main(workers_number, save_result, delete_duplicate)
    end_time = datetime.now()

    print(f"proccess duration: {end_time - start_time}")
