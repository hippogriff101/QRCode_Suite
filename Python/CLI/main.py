import qrcode, random
img = qrcode.make(input("enter link: "))
type(img)
filename = f"qrcode_suite{random.randint(1,1000)}.png"
img.save(filename)
print(f"QR code generated and saved successfully as '{filename}'.")