#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from django.core.management import execute_from_command_line

ALLOWED_HOSTS = ['*']
def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
