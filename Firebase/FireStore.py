import Firebase
from datetime import datetime 

class Firestore:
    def __init__(self, collection_name):
        self.db = Firebase.store
        self.collection_name = collection_name
        self.num_documents = self._get_num_documents()
        self.last_updated_date = None

    def _get_num_documents(self):
        docs = self.db.collection(self.collection_name).stream()
        return len(list(docs))
    
    def _update_last_updated_date(self):
        self.last_updated_date = datetime.now()
    
    def add_document(self, data):
        try:
            doc_ref = self.db.collection(self.collection_name).add(data)
            self.num_documents += 1
            self._update_last_updated_date()
            return {'id': doc_ref.id}  # Ensure this is a dictionary with 'id'
        except Exception as e:
            print(f'An error occurred while adding document: {e}')
            return None
    
    def add_document_with_id(self, doc_id, data):
        try:
            doc_ref = self.db.collection(self.collection_name).document(doc_id)
            doc_ref.set(data)
            self.num_documents += 1
            self._update_last_updated_date()
            return {'id': doc_id}
        except Exception as e:
            print(f'An error occurred while adding document with ID {doc_id}: {e}')
            return None
    
    def remove_document(self, doc_id):
        try:
            doc_ref = self.db.collection(self.collection_name).document(doc_id)
            doc_ref.delete()
            self.num_documents -= 1
            self._update_last_updated_date()
            print(f'Document {doc_id} deleted successfully')
        except Exception as e:
            print(f'An error occurred while deleting document {doc_id}: {e}')
    
    def fetch_all_documents(self):
        try:
            docs = self.db.collection(self.collection_name).stream()
            doc_list = [{doc.id: doc.to_dict()} for doc in docs]
            return doc_list
        except Exception as e:
            print(f'An error occurred while fetching all documents: {e}')
            return None
    
    def fetch_document_by_id(self, doc_id):
        try:
            doc_ref = self.db.collection(self.collection_name).document(doc_id)
            doc = doc_ref.get()
            if doc.exists:
                return doc.to_dict()
            else:
                print(f'No such document with ID {doc_id}')
                return None
        except Exception as e:
            print(f'An error occurred while fetching document {doc_id}: {e}')
            return None
    
    def search_by_keyword(self, field, keyword):
        try:
            docs = self.db.collection(self.collection_name).where(field, '==', keyword).stream()
            results = [{doc.id: doc.to_dict()} for doc in docs]
            return results
        except Exception as e:
            print(f'An error occurred while searching by keyword {keyword} in field {field}: {e}')
            return None
    
    def update_document(self, doc_id, data):
        try:
            doc_ref = self.db.collection(self.collection_name).document(doc_id)
            doc_ref.update(data)
            self._update_last_updated_date()
            print(f'Document {doc_id} updated successfully')
        except Exception as e:
            print(f'An error occurred while updating document {doc_id}: {e}')
    
    def select_with_conditions(self, conditions):
        try:
            query = self.db.collection(self.collection_name)
            for field, value in conditions.items():
                query = query.where(field, '==', value)
            docs = query.stream()
            results = [{doc.id: doc.to_dict()} for doc in docs]
            return results
        except Exception as e:
            print(f'An error occurred while selecting documents with conditions {conditions}: {e}')
            return None
        

