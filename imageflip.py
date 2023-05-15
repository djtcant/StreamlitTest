import streamlit as st
import PIL
from PIL import Image
st.title("PHOTO EDITING APP")
file = st.file_uploader("Upload photo", type=["jpg", "png"])
if file != None:
    display= st.image (file, width=250)
    img = PIL.Image.open(file)
    
if st.button("Flip Image"):
    conv_img = img.transpose(Image.FLIP_TOP_BOTTOM)
    display.image (conv_img, width=250)

if st.button("Change Colour"):
    pix = img.load()
    new_image = Image.new(img.mode, (img.width, img.height))
    new_pix_map = new_image.load()

    for r_i in range(img.size [1]):
        for c_i in range(img.size[0]):
            if r_i < 100 and c_i< 100:
                new_pix_map[c_i, r_i] = (255, 0, 0) 
            else:
                new_pix_map[c_i, r_i] = pix[c_i, r_i]
    
    display.image (new_image, width=250)