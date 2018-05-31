import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings.dev')
import django
django.setup()

from django.contrib.auth.models import User
from django.utils import timezone
import requests
import datetime
import random
import string
import json
import sys
import os

from blog.models import Post, Tag


# generators api
# names  http://names.drycodes.com/500?nameOptions=boy_names,girl_names
# images https://source.unsplash.com/random
# text "https://loripsum.net/api/10/plaintext