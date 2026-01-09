import qrcode, time
number = 1
def main():
    global number
    img = qrcode.make(input("Please enter the link you want to make to a qrcode: "))
    filename = f"qrcode_suite{number}.png"
    img.save(filename)
    print(f"QR code generated and saved successfully as '{filename}'.")
    number += 1
if __name__ == "__main__":
    time.sleep(0.5)
    print("=========================================")
    time.sleep(0.5)
    print(r"""
   ____  _____     _____          _         _____       _ _       
  / __ \|  __ \   / ____|        | |       / ____|     (_) |      
 | |  | | |__) | | |     ___   __| | ___  | (___  _   _ _| |_ ___ 
 | |  | |  _  /  | |    / _ \ / _` |/ _ \  \___ \| | | | | __/ _ \
 | |__| | | \ \  | |___| (_) | (_| |  __/  ____) | |_| | | ||  __/
  \___\_\_|  \_\  \_____\___/ \__,_|\___| |_____/ \__,_|_|\__\___|
""")
    time.sleep(0.5)
    print("      QR Code Suite - CLI Version       ")
    text = "     Created by Freddie Yershon         "
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.1)
    print("")
    time.sleep(0.5)
    print("Welcome to the QR Code Suite CLI Version!")
    time.sleep(0.5)
    print("=========================================")
    time.sleep(1)
    main()
    while True:
        again = input("Do you want to create another QR code? (yes/no): ").strip().lower()
        if again == 'yes':
            main()
        elif again == 'no':
            print("Thank you for using the QR Code Suite CLI Version. Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")