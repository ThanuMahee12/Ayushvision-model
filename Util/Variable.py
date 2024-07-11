import os
from datetime import date
from dotenv import load_dotenv, dotenv_values 
load_dotenv() 
# Enviroment Variable
original_dataset_dir=os.getenv('MAIN_DATASET_PATH')
summary_report_dir=os.environ.get('SUMMARY_DICTORY')

#
# ayush_vision_json=
today=date.today()
today_summary_path=os.path.join(summary_report_dir,today.strftime('%Y_%m_%d'))

working_dirctory=os.getenv("TARGET_DATASET_PATH")
working_dir_name=os.getenv('WORKING_DIR_NAME')
ayush_classFication_Working=os.path.join(working_dirctory,working_dir_name,'classification')
ayush_detection_Working=os.path.join(working_dirctory,working_dir_name,'detection')