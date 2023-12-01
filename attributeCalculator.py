import numpy
import rasterio
from rasterio.plot import reshape_as_image
from fastapi.responses import FileResponse
from PIL import Image
from pathlib import Path

def get_width(image_path):
    with rasterio.open(image_path) as image:
        width = image.width
         
    return width

def get_heigth(image_path):
    with rasterio.open(image_path) as image:
        height = image.width
         
    return height

def get_num_bands(image_path):
    with rasterio.open(image_path) as image:
        num_bands = image.count
         
    return num_bands

def get_crs(image_path):
    with rasterio.open(image_path) as image:
        crs = image.crs
         
    return crs

def get_bounding_box(image_path):
    with rasterio.open(image_path) as image:
        bounding_box = image.bounds
         
    return bounding_box

def convertToPng(image_path):
    with rasterio.open(image_path) as image:
        rgb_bands = image.read([1,2,3])
        thumbnail_size=(256,256)
        
        rgb_bands = (rgb_bands / rgb_bands.max())*255
        rgb_bands = rgb_bands.astype('uint8')
        img_rgb = reshape_as_image(rgb_bands)
        img_thumbnail = Image.fromarray(img_rgb).resize(thumbnail_size)
        
        output_path = Path.cwd() / "output_thumbnail.png"
        img_thumbnail.save(output_path, format="PNG")
        
        return FileResponse(path=output_path, filename="output_thumbnail.png")