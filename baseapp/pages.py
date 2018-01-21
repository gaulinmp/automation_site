# -*- coding: utf-8 -*-
from flask import render_template, jsonify


from . import app
from .broadlink import blink

################################################################################
####           Routes                                                       ####
################################################################################

@app.route('/')
def home():
    return render_template('pages/index.html', 
            data={'devices': blink.get_device_dict()})

@app.route('/send/<string:device>/<string:command>')
def send(device, command):
    return jsonify({'success': blink.send_command(device, command)})
