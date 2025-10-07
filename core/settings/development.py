from .base import *
DEBUG = True
#INSTALLED_APPS += ['django_debugger', 'debug_toolbar']
#MIDDLEWARE = ['debug_toolbar.middleware.DebugToolbarMiddleware', *MIDDLEWARE]

ALLOWED_HOSTS += ["mysite-1ofp.onrender.com"]


import os
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST', 'mail.yourdomain.com')
EMAIL_PORT = os.getenv('EMAIL_PORT', 587)
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', True)
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', 'noreply@yourdomain.com')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', 'your-email-password')
# Isah was here =__>>> Add this at the end of the file

# In development.py - replace your current FILE_UPLOAD_HANDLERS with:
FILE_UPLOAD_HANDLERS = [
    'django.core.files.uploadhandler.MemoryFileUploadHandler',
]

# Reduce memory size to ensure files stay in memory
FILE_UPLOAD_MAX_MEMORY_SIZE = 2097152  # 2MB
DATA_UPLOAD_MAX_MEMORY_SIZE = 2097152  # 2MB

# Add this at the VERY END of development.py
import django.core.files.locks

# Completely disable file locking
def dummy_lock(fd, flags):
    return True

def dummy_unlock(fd):
    return True

# Monkey patch the locking functions
django.core.files.locks.lock = dummy_lock
django.core.files.locks.unlock = dummy_unlock

# Also patch the file storage
from django.core.files.storage import FileSystemStorage

original_save = FileSystemStorage._save

def patched_save(self, name, content):
    """
    Modified _save that completely bypasses file locking
    """
    import os
    full_path = self.path(name)
    
    # Create directory if it doesn't exist
    directory = os.path.dirname(full_path)
    if not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)
    
    # Save file directly without any locking
    with open(full_path, 'wb') as destination:
        for chunk in content.chunks():
            destination.write(chunk)
    
    # Ensure file permissions
    if not os.access(full_path, os.W_OK):
        os.chmod(full_path, 0o644)
    
    return name

# Apply the patch
FileSystemStorage._save = patched_save