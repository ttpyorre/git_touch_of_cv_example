import glob

def extract_images():
    filename_list = []
    for image in glob.glob('**/*.jpg'):
        filename_list.append(image)
    return filename_list

