"""
WSGI config for blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings")

application = get_wsgi_application()
"""
import sys

sys.path.append('D:/gxyd/bomc_i')
# 加入本项目的虚拟环境(当两个django项目使用不同版本时，这可能非常有用)
virtualenv_dir = 'D:/gxyd/bomc_i/venv/Lib/site-packages'  # 虚拟环境python包文件夹
sys.path.insert(0, virtualenv_dir)  # 加入导包路径
"""