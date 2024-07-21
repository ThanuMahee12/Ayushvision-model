import os

from dotenv import load_dotenv, dotenv_values 
load_dotenv() 
# Enviroment Variable
original_dataset_dir=os.getenv('MAIN_DATASET_PATH')
summary_report_dir=os.environ.get('SUMMARY_DICTORY')
firebaseKey=os.environ.get('FIREBASEKEY')

