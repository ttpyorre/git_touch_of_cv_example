import glob

def extract_images(dir_name):
    filename_list = []
    for image in glob.glob('./*', '.jpg'):
        filename_list.append(image)
    return filename_list

