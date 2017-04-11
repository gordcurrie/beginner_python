import os
import cat_service
import subprocess
import platform


def main():
    print_header()
    folder = get_or_create_output_folder()
    download_cats(folder)
    display_cats(folder)


def print_header():
    print('--------------------------')
    print('     LOLCat APP')
    print('--------------------------')


def get_or_create_output_folder():
    base_folder = os.path.dirname(__file__)
    folder = 'cat_pictures'
    full_path = os.path.join(base_folder, folder)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('Creating new directory at {}'. format(full_path))
        os.makedirs(full_path)

    return full_path



def download_cats(folder):
    print("Fetching cats...")
    cat_count = 8
    for i in range(1, cat_count + 1):
        name = 'lolcat_{}'.format(i)
        print("{}...".format(name))
        cat_service.get_cat(folder, name)

    print("Cats downloaded")


def display_cats(folder):
    system = platform.system()
    if system == 'Darwin':
        subprocess.call(['open', folder])
    elif system == 'Windows':
        subprocess.call(['explorer', folder])
    elif system == 'Linux':
        subprocess.call(['xdg-open', folder])
    else:
        print("We don't support your os: " + system)


if __name__ == '__main__':
    main()