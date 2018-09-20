# -*- coding: utf-8 -*-
from flask import render_template, jsonify


from . import app
from .broadlink import blink

################################################################################
####           Routes                                                       ####
################################################################################

@app.route('/')
def home():
    icons = [
        ('volume_up', 'volume_up.svg' ), 
        ('volume_down', 'volume_down.svg' ), 
        ('sat-catv', 'chromecast.svg' ), 
        ('stb', 'computer.svg' ), 
        ('game', 'ps4.svg' ), 
        ('video', 'switch.svg' ), 
    ]
    return render_template('pages/index.html', 
            data={'devices': blink.get_device_dict(),
                  'icons': icons})

@app.route('/send/<string:device>/<string:command>')
def send(device, command):
    return jsonify({'success': blink.send_command(device, command)})
