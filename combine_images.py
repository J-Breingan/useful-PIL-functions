# -*- coding: utf-8 -*-
"""
Created on Mon May 24 20:54:08 2021

@author: Jack
"""
from PIL import Image

def polygonal_paste(image_1, image_2, polygon_1, polygon_2):
    """
    "Combines two images, inserting image_2 into a region defined by the polygons"
    
    Args
    -----------------
    image_1 & 2: a pillow Image, each must have the same dimensions as the other
    polygon_1: the area of image_2 that will be used in the final result
    polygon_2: the area of image_1 that will be used
    
    """    
    
    #trim images
    mask = Image.new("L", original.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.polygon(polygon_1, fill=255, outline=None)
    a = Image.composite(image_1, Image.new("L", original.size, 255), mask)

    mask = Image.new("L", original.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.polygon(polygon_2, fill=255, outline=None)
    b = Image.composite(image_2, Image.new("L", original.size, 255), mask)
    
    
    #create mask
    im_a = Image.new("L", image_1.size, 0)#.convert("RGB")
    draw = ImageDraw.Draw(im_a)
    draw.polygon(xy_2, fill=255)
    
    #mask image with transparency
    im_alpha = b.copy().convert("RGB")
    im_alpha.putalpha(im_a)
    
    #merge the images
    a.paste(im_alpha, (0,0), im_alpha)
    
    return a

def concat_horizontally(image_1, image_2):
    """Concatentates 2 images horizontally
    Args
    ----------------
    image_1, image_2: pillow Images with equal vertical dimensions"""
    
    #create background
    bg = Image.new("L", (image_1.size[0] + image_2.size[0], image_1.size[1]), "white")
    #paste images onto background
    bg.paste(image_1, (0,0))
    bg.paste(image_2, (image_1.size[0],0))
    
    return bg

def concat_inverted_triangle(tl, tr, bc):
    """
    Combine three images in a point-down triangle
    
    Args
    ---------------------
    tl = top left image
    tr = top right image
    bc = bottom centre image"""
    
    #create background
    bg = Image.new("L",(tl.size[0]*2, tl.size[1]*2), "white")
    #paste images onto background
    bg.paste(tl, (0,0))
    bg.paste(tr, (tl.size[0],0))
    bg.paste(bc, (int(tl.size[0]/2),tl.size[1]))
    
    return bg

def concat_matrix(images):
    """Given a list, nxm, of images, concat them into one image.
    Each image must be the same size. Each list in images represents one row, and
    each must be the same size (or at least smaller than the first)
    
    Args
    -------------------
    images: a list of lists of pillow Images
    """
    #get image dimensions in px
    img_x, img_y = images[0][0].size
    #get number of columns and rows
    num_cols = len(images[0])
    num_rows = len(images)
    
    #create background
    bg = Image.new("L", (img_x * num_cols, img_y * num_rows), "white")
    
    #iterate over rows and columns, adding images
    y=0
    for row in images:
        x = 0
        for image in row:
            bg.paste(image, (x,y))

            x += img_x

        y += img_y
        
    return bg