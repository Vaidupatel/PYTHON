import qrcode 
# from PIL import Image

def qr_generate(data, fill_color="black", back_color="white", border_size=4, box_size=100, image_name="MyQRCode", extension="png"):

    qr = qrcode.QRCode(version = 1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=box_size,border = border_size)


    qr.add_data(data)
    qr.make(fit = True)

    img = qr.make_image(fill_color =fill_color,back_color =back_color)
    img_name = f"{image_name}.{extension}"
    img.save(img_name)

def main():

    data = input("Enter the data for the QR code: ")
    fill_color = input("Enter the fill color for the QR code (black): ") or "black"
    back_color = input("Enter the background color for the QR code (white): ") or "white"
    border_size = input("Enter the border size for the QR code (default: 4): ")
    if border_size:
        border_size = int(border_size)
    else:
        border_size = 4
    box_size = input("Enter the box size for the QR code (default: 100): ")
    if box_size:
        box_size = int(box_size)
    else:
        box_size = 100
    image_name = input("Enter the name of the image to save (MyQRCode): ") or "MyQRCode"
    extension = input("Enter the extension name of the image (png): ") or "png"

    qr_generate(data, fill_color, back_color, border_size, box_size, image_name, extension)


if __name__ == "__main__":
    main()
