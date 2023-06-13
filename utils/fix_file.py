from urllib.parse import urlparse

def change_img_src(url):
    parsed = urlparse(url)
    path_parts = parsed.path.split('/')
    filename = path_parts[-1]
    new_path = f"images/products/{filename}"
    return new_path
 