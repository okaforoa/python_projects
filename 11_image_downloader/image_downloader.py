import os
import requests


def get_extension(image_url: str) -> str:
    # Create a list of popular extensions to check for
    extensions = ['.png', '.jpg', '.jpeg', '.gif', '.svg']

    # Check that the extension exists inside the URL
    for ext in extensions:
        if ext in image_url:
            return ext
    return None


def download_image(image_url: str, name: str, folder: str = None):
    """Download the image from any given url"""

    # Attempt to get the correct image extension from an url
    ext = get_extension(image_url)
    if ext:
        if folder:
            if not os.path.exists(folder):
                os.makedirs(folder)
            image_name = os.path.join(folder, f'{name}{ext}')
        else:
            image_name = f'{name}{ext}'
    else:
        raise Exception('Image extension could not be located...')

    # Check if the name already exists
    if os.path.isfile(image_name):
        raise Exception('File name already exists...')

    try:
        # Get the image as bytes and write it locally to our computer
        response = requests.get(image_url)
        response.raise_for_status()
        with open(image_name, 'wb') as handler:
            handler.write(response.content)
            print(f'Downloaded: "{image_name}" successfully!')
    except Exception as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    # Sample URLs
    # image_url_1 = 'https://media.istockphoto.com/id/184276818/photo/red-apple.jpg?s=612x612&w=0&k=20&c=NvO-bLsG0DJ_7Ii8SSVoKLurzjmV0Qi4eGfn6nW3l5w=' # NOQA
    # image_url_2 = 'https://w.wallhaven.cc/full/1p/wallhaven-1p398w.jpg'
    # image_url_3 = 'https://www.svgrepo.com/show/376344/python.svg'

    # Get the user input for the download
    input_url = input('Enter a URL: ')
    input_name = input('What would you like to name it?: ')

    # Download the image
    print('Downloading...')
    download_image(input_url, name=input_name, folder='images')
