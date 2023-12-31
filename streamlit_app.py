import streamlit as st
from pathlib import Path as path
from moviepy.editor import VideoFileClip
from processes.process import process
import shutil
import os

st.title("Deep Fake Generator!!!!!")
st.header("yipee!!!")

with st.form(key="Form :", clear_on_submit= True):

    img = st.file_uploader(label="upload the image you want to deepfake")
    temp = st.file_uploader(label="upload the template you would like to use")
    submit = st.form_submit_button(label="submit")

if submit:

    st.write("Processing... Please allow up to 15 minutes for your request to process.")
    img_path = path("./saved", img.name)
    temp_path = path("./saved", temp.name)
    with open(img_path, mode="wb") as w:
        w.write(img.getvalue())
    with open(temp_path, mode="wb") as w:
        w.write(temp.getvalue())
        

    if img_path.exists() and temp_path.exists():  

        len_vid = VideoFileClip(f"./saved/{temp.name}").duration
        st.write("video length: " + str(len_vid))

        if len_vid <= 30:
            process.generate(img.name, temp.name)

            img_name = img.name.partition(".")
            video_file = open(f'./generated/{img_name}.mp4', "rb")
            video_bytes = video_file.read()

            st.video(video_bytes)
        else:
            st.write("Error! Make sure that your template video is less than 30 seconds in length!")

