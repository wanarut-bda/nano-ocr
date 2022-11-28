from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
from pywebio.pin import *
from pywebio import start_server
import os

import yaml
from yaml.loader import SafeLoader

# Open the file and load the file
with open('config.yaml') as f:
    data = yaml.load(f, Loader=SafeLoader)


def login_page():
    while (True):
        login = input_group("login", [
            input('username', name='username', type=TEXT),
            input('password', name='password', type=TEXT),
        ])

        if (login['username'] == data['username']
                and login['password'] == data['password']):
            break
        toast("Incorrect uesrname or password", color='red')


def config_page():
    web_html = open("web_html2.html", "r").read()
    img = open('cur_pic.bmp', 'rb').read()
    put_image(img, width='1280px')
    put_html(web_html)
    os.system('reboot')


def main():  # PyWebIO application function
    login_page()

    mqtt = input_group("mqtt broker (can skip by cancel button)", [
        input('host', name='host', type=TEXT),
        input('port', name='port', type=TEXT),
    ],
                       cancelable=True)

    config_page()


if __name__ == '__main__':
    start_server(main, 80)