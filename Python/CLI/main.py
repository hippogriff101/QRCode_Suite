import qrcode
no = 1
img = qrcode.make(input("enter link: "))
filename = f"qrcode_suite{no}.png"
img.save(filename)
print(f"QR code generated and saved successfully as '{filename}'.")