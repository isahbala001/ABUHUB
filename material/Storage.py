# material/storage.py
""" import os
from django.core.files.storage import FileSystemStorage
from django.core.files import locks as file_locks

class NoLockFileSystemStorage(FileSystemStorage):
    def _save(self, name, content):
        """
        Custom save method that completely bypasses file locking
        """
        full_path = self.path(name)
        
        # Create directory if it doesn't exist
        directory = os.path.dirname(full_path)
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
        
        # Save the file without any locking mechanism
        try:
            # Write the file directly without using Django's locking
            with open(full_path, 'wb') as destination:
                for chunk in content.chunks():
                    destination.write(chunk)
        except IOError as e:
            # If there's an IO error, fall back to parent method
            return super()._save(name, content)
        
        # Ensure the file is writable
        if not os.access(full_path, os.W_OK):
            os.chmod(full_path, self.file_permissions_mode)
        
        return name """