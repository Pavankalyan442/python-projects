import qrcode
data=input("Enter the url or text:").strip()
file_name=input("enter the file name:").strip()
qr=qrcode.QRCode(box_size=10,border=4)
qr.add_data(data)
image=qr.make_image(fill_color="black",back_color="white")
image.save(file_name)
print(f"Qr Code save as {file_name}")