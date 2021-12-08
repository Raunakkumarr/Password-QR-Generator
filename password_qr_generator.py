import random
import qrcode

def generate_password(n_chracters):
    lower='abcdefghijklmnopqrstuvwxyz'
    upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers='12345678901234567890'
    symbols='!"#$%&/()={}[]'
    all_characters=lower+upper+numbers+symbols
    password=''.join(random.sample(all_characters, n_chracters))
    return password

def image_qr(password):
    filename=input('Name Password: ')
    img=qrcode.make(password)
    img.save(filename+'.png')
    #print(f'Your Password is "{password}"')
    print(f"The password was saved as {filename}.png in the current working directory.")

def run():
    characters=int(input('Digit Number of Characters: '))
    password=generate_password(characters)
    image_qr(password)

if __name__ == '__main__':
    run()
