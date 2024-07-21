import os
from datetime import date
from dotenv import load_dotenv, dotenv_values 
load_dotenv() 
# Enviroment Variable
original_dataset_dir=os.getenv('MAIN_DATASET_PATH')
summary_report_dir=os.environ.get('SUMMARY_DICTORY')
working_dirctory=os.getenv("TARGET_DATASET_PATH")
working_dir_name=os.getenv('WORKING_DIR_NAME')
firebaseKey=os.environ.get('FIREBASEKEY')

#
# ayush_vision_json=
today=date.today()
todaysummaryKey=today.strftime('%Y_%m_%d')
today_summary_path=os.path.join(summary_report_dir,today.strftime('%Y_%m_%d'))
today_classfication_analysis_path=os.path.join(today_summary_path,'analysis','classfication') # from Variables
today_classfication_non_eligble_csv=os.path.join(today_classfication_analysis_path,'classification_non_elible.csv')

ayush_classFication_Working=os.path.join(working_dirctory,working_dir_name,'classification')
ayush_detection_Working=os.path.join(working_dirctory,working_dir_name,'detection')

