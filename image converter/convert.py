from PIL import Image
#convert webp to png
# im=Image.open("hi.webp").convert("RGB")
# im.save("hii.png","png")

#convert png to webp
im=Image.open("hii.png").convert("RGB")
im.save("hii.webp","webp")


# im=Image.open("hi.webp").convert("RGB")
# im.save("hii.png","png")