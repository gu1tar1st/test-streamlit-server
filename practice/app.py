# Add model to Streamlit server

import streamlit as st
import boto3
import os
from transformers import pipeline
import torch

s3_client = boto3.client('s3')
bucket_name = 'vdnk-mlops-test-bucket'
s3_prefix = 'model/custom-tinybert-sentiment-analysis'
local_dir = '08-Deploy_ML_Model_at_Streamlit_Server/model/tinybert-sentiment-analysis'

def download_folder(local_dir: str, s3_prefix: str):
    os.makedirs(local_dir, exist_ok=True)
    paginator = s3_client.get_paginator('list_objects_v2')
    for result in paginator.paginate(Bucket=bucket_name, Prefix=s3_prefix):
        if 'Contents' in result:
            for key in result['Contents']:
                s3_key = key['Key']
                local_file = os.path.join(local_dir, os.path.relpath(s3_key, s3_prefix))
                s3_client.download_file(bucket_name, s3_key, local_file)

st.title("ML Model Streamlit Host to Download model from S3")

button = st.button("Download your model")
if button:
    with st.spinner("Download, please wait!"):
        download_folder(local_dir, s3_prefix)

# Testing prediction
device = torch.device('cpu')
classifier = pipeline(
    task='text-classification',
    model="08-Deploy_ML_Model_at_Streamlit_Server/model/tinybert-sentiment-analysis",
    device=device,
)


st.subheader("")
st.subheader("Testing your model")
user_input = st.text_area(
    label='Enter your test review',
    placeholder='Type here',
)
predict = st.button('Predict')

if predict:
    with st.spinner('Predicting...'):
        prediction = classifier(user_input)
    st.write(f'Predict: {prediction[0]['label']}')