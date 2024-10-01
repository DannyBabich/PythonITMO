# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u2840741/data/www/gallerydept.ru/')
sys.path.insert(1, '/var/www/u2840741/data/gallerydept/lib/python3.10/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'store.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
