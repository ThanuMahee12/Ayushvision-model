from datetime import datetime
import Firebase
import os
class FireStorage:
    def __init__(self, folder_name):
        self.bucket = Firebase.storageBudget
        self.folder_name = folder_name
        self.last_updated_date = None

    def _update_last_updated_date(self):
        self.last_updated_date = datetime.now()
    
    def create_subfolder(self, subfolder_name):
        # Subfolders are simulated by uploading a dummy file
        try:
            dummy_file_path = f"{self.folder_name}/{subfolder_name}/.dummy"
            blob = self.bucket.blob(dummy_file_path)
            blob.upload_from_string('')  # Upload an empty file to create a "folder"
            self._update_last_updated_date()
            print(f"Subfolder '{subfolder_name}' created successfully.")
        except Exception as e:
            print(f"An error occurred while creating subfolder: {e}")

    def delete_subfolder(self, subfolder_name):
        try:
            blobs = self.bucket.list_blobs(prefix=f"{self.folder_name}/{subfolder_name}/")
            for blob in blobs:
                blob.delete()
            self._update_last_updated_date()
            print(f"Subfolder '{subfolder_name}' deleted successfully.")
        except Exception as e:
            print(f"An error occurred while deleting subfolder: {e}")

    def rename_subfolder(self, old_subfolder_name, new_subfolder_name):
        try:
            blobs = self.bucket.list_blobs(prefix=f"{self.folder_name}/{old_subfolder_name}/")
            for blob in blobs:
                new_name = blob.name.replace(f"{self.folder_name}/{old_subfolder_name}/", f"{self.folder_name}/{new_subfolder_name}/")
                new_blob = self.bucket.blob(new_name)
                new_blob.rewrite(blob)
                blob.delete()
            self._update_last_updated_date()
            print(f"Subfolder '{old_subfolder_name}' renamed to '{new_subfolder_name}' successfully.")
        except Exception as e:
            print(f"An error occurred while renaming subfolder: {e}")

    def add_photo(self, file_path):
        try:
            if not os.path.isfile(file_path):
                raise FileNotFoundError(f"The file {file_path} does not exist.")
            
            file_name = os.path.basename(file_path)
            blob = self.bucket.blob(f"{self.folder_name}/{file_name}")
            blob.upload_from_filename(file_path)
            self._update_last_updated_date()
            print(f"Photo {file_name} added successfully.")
            return {'name': file_name, 'url': blob.public_url}
        except Exception as e:
            print(f"An error occurred while adding photo: {e}")
            return None
    def get_photo(self, file_name):
        try:
            blob = self.bucket.blob(f"{self.folder_name}/{file_name}")
            if blob.exists():
                return blob.public_url
            else:
                print(f"Photo {file_name} not found.")
                return None
        except Exception as e:
            print(f"An error occurred while getting photo: {e}")
            return None

    def delete_photo(self, file_name):
        try:
            blob = self.bucket.blob(f"{self.folder_name}/{file_name}")
            if blob.exists():
                blob.delete()
                self._update_last_updated_date()
                print(f"Photo {file_name} deleted successfully.")
            else:
                print(f"Photo {file_name} not found.")
        except Exception as e:
            print(f"An error occurred while deleting photo: {e}")

    def update_photo(self, old_file_name, new_file_path):
        try:
            self.delete_photo(old_file_name)
            return self.add_photo(new_file_path)
        except Exception as e:
            print(f"An error occurred while updating photo: {e}")
            return None

    def search_by_name(self, search_name):
        try:
            blobs = self.bucket.list_blobs(prefix=self.folder_name)
            results = [blob.name for blob in blobs if search_name in blob.name]
            return results
        except Exception as e:
            print(f"An error occurred while searching for photos: {e}")
            return None
        
