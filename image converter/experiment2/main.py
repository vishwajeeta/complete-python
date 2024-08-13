from PIL import Image

im=Image.open("amazon.png").convert("RGB")
im.save("amazon.webp","webp")

im=Image.open("asvsi.png").convert("RGB")
im.save("asvsi.webp","webp")

im=Image.open("digital_products.png").convert("RGB")
im.save("digital_products.webp","webp")


im=Image.open("Next_portfolio.png").convert("RGB")
im.save("Next_portfolio.webp","webp")

im=Image.open("portfolio.png").convert("RGB")
im.save("portfolio.webp","webp")

im=Image.open("sambhram.png").convert("RGB")
im.save("sambhram.webp","webp")

im=Image.open("transfer.png").convert("RGB")
im.save("transfer.webp","webp")