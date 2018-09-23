# -*- coding: utf-8 -*-
from flask import render_template, jsonify


from . import app
from .broadlink import blink

################################################################################
####           Routes                                                       ####
################################################################################

@app.route('/')
def home():
    devices = [ 
        # Outer list: sections
        # Inner list: (device-name, command-name, icon-name)
        [ # Section 1: Visio TV
            ('vizio-tv', 'power', 'new_tv.svg'),
            ('vizio-tv', 'volume_up', 'volume_up.svg'), 
            ('vizio-tv', 'volume_down', 'volume_down.svg'),
            ('sony-reciever', 'main_sat-catv', 'chromecast.svg'),
            ('sony-reciever', 'main_stb', 'computer.svg'),
            ('sony-reciever', 'main_game', 'ps4.svg'),
            ('sony-reciever', 'main_video', 'switch.svg'),
        ],
        [  # Section 1: Samsung TV
            ('samsung-tv', 'power', 'old_tv.svg'),
            ('samsung-tv', 'volume_up', 'volume_up.svg'),
            ('samsung-tv', 'volume_down', 'volume_down.svg'),
            ('sony-reciever', 'zone2_sat-catv', 'chromecast.svg'),
            ('sony-reciever', 'zone2_stb', 'computer.svg'),
            ('sony-reciever', 'zone2_game', 'ps4.svg'),
            ('sony-reciever', 'zone2_video', 'switch.svg'),
        ],
        [  # Section 1: Sony Receiver
            ('sony-receiver', 'power', 'receiver.jpg'),
            ('sony-receiver', 'volume_up', 'volume_up.svg'),
            ('sony-receiver', 'volume_down', 'volume_down.svg'),
        ]
    ]
    return render_template('pages/index.html', 
            data={'all_devices': blink.get_device_dict(),
                  'devices': devices, 
                  })

@app.route('/send/<string:device>/<string:command>')
def send(device, command):
    return jsonify({'success': blink.send_command(device, command)})
