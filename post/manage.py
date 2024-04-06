#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from managepost.consumer import consume_messages
import threading
import django

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'post.settings')
    
    django.setup()
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
        
        
    def consumertask():
        while True:
            consume_messages()

    background_thread = threading.Thread(target=consumertask)
    background_thread.daemon = True
    background_thread.start()
    
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
