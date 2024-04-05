# -*- coding: utf-8 -*-
# vim: ft=python:
# @module index.wsgi
# @desc Django wsgi start script
# @since 2024.03.06, 20:47
# @changed 2024.04.05, 18:38

import os
import sys
import time
import traceback
import signal
from pathlib import Path

# App root path
rootPath = os.path.dirname(os.path.abspath(__file__))

# Detect home path...
home = str(Path.home())

# TODO: Get the venv path from config?
activate_this = home + '/.virtualenv/bin/activate_this.py'
with open(activate_this) as f:
    code = compile(f.read(), activate_this, 'exec')
    exec(code, dict(__file__=activate_this))

# Inject application path...
sys.path.insert(1, rootPath)

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dds_registration.settings')
from django.core.wsgi import get_wsgi_application

try:
    application = get_wsgi_application()
except RuntimeError:
    traceback.print_exc()
    os.kill(os.getpid(), signal.SIGINT)
    time.sleep(2.5)
