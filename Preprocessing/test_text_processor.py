#Not elegant !!
import sys
sys.path.append("../")

from Preprocessing.TransformData.TextProcessor import TextProcessor
import pandas as pd 
from Env.ProjectPaths import *
glassdoor_df = pd.read_csv(GLASSDOOR_JOB_DESCRIPTIONS_DATASET_PATH)
kaggle_df = pd.read_csv(KAGGLE_JOB_DESCRIPTIONS_DATASE_PATHT)









glassdoor_text_processor = TextProcessor(col='Job Description')

glassdoor_descrptions_preprocessed = glassdoor_text_processor.process_data(glassdoor_df)

kaggle_text_processor = TextProcessor(col='description')

kaggle_descriptions_preprocessed = kaggle_text_processor.process_data(kaggle_df)


kaggle_job_descriptions = kaggle_descriptions_preprocessed[['description']]
kaggle_job_descriptions.columns=  ['Job Description']

glassdoor_job_descriptions = glassdoor_descrptions_preprocessed[['Job Description']]




job_descriptions = pd.concat([kaggle_job_descriptions, glassdoor_job_descriptions])


print(job_descriptions)
