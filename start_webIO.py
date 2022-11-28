from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
from pywebio.pin import *
from pywebio import start_server, config
import os

import yaml
from yaml.loader import SafeLoader

config(title="OCR Setting")
# Open the file and load the file
with open('./yaml/admin.yaml') as file:
    admin_yaml = yaml.load(file, Loader=SafeLoader)

def reboot_system():
    confirm = actions('Confirm to Reboot?', ['confirm', 'cancel'],
                      help_text='Wait 1 minute for restart')
    if confirm=='confirm':  
        os.system('reboot')


def login_page():
    while (True):
        login = input_group("login", [
            input('username', name='username', type=TEXT, required=True),
            input('password', name='password', type=PASSWORD, required=True),
        ])

        if (login['username'] == admin_yaml['username']
                and login['password'] == admin_yaml['password']):
            break
        toast("Incorrect uesrname or password", color='red')


def change_password():
    password = input_group("enter new password (can skip by cancel button)", [
        input('new password', name='password', type=TEXT, required=True),
        input('new password again', name='re_password', type=TEXT, required=True),
    ], cancelable=True)

    if password is not None:
        if (password['password'] == password['re_password']):
            print(password)
            # save password
            admin_yaml['password'] = password['password']
            with open('./yaml/admin.yaml', 'w') as file:
                yaml.dump(admin_yaml, file)
        else:
            toast("password does not match", color='red')
            change_password()


def mqtt_page():
    with open('./yaml/mqtt.yaml') as f:
        mqtt_config = yaml.load(f, Loader=SafeLoader)

    mqtt = input_group("mqtt broker (can skip by cancel button)", [
        input('host', name='host', type=TEXT, required=True, value=mqtt_config['host']),
        input('port', name='port', type=TEXT, required=True, value=mqtt_config['port']),
        input('topic', name='topic', type=TEXT, required=True, value=mqtt_config['topic']),
        input('username', name='username', type=TEXT, value=mqtt_config['username']),
        input('password', name='password', type=PASSWORD),
    ], cancelable=True)

    if mqtt is not None:
        with open('./yaml/mqtt.yaml', 'w') as file:
            yaml.dump(mqtt, file)


def config_page():
    web_html = open("web_config.html", "r").read()
    img = open('cur_pic.bmp', 'rb').read()
    put_image(img, width='1280px')
    put_html(web_html)
    put_button('reboot', onclick=reboot_system, small=True)


def main():  # PyWebIO application function
    login_page()
    change_password()
    mqtt_page()
    config_page()


if __name__ == '__main__':
    start_server(main, port=80, debug=True)