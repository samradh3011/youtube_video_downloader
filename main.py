import streamlit as st
from pytube import YouTube

bg_color = """
<style>
body {
background-color: cyan;
background-size: cover;
}
</style>
"""
st.markdown(bg_color, unsafe_allow_html=True)

youtube_url = st.text_area('Enter Youtube Video URL')
if youtube_url != '':
    try:
        yt_obj = YouTube(youtube_url)
        filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')
        # download the highest quality video
        filters.get_highest_resolution().download(output_path='C://Users//Public//high_resolution_videos_st//', filename=f'{yt_obj.title[0:5]}')
        st.header('Video Downloaded Successfully')
        st.sidebar.write(f'Video Title: **{yt_obj.title}**')
        st.sidebar.write(f'Video Length: **{yt_obj.length}** Seconds')
        st.sidebar.write(f'Video View Count: **{yt_obj.views}**')
        st.sidebar.write(f'Video Uploaded by: **{yt_obj.author}**')
        video = st.video(f'C://Users//Public//high_resolution_videos_st//{yt_obj.title[0:5]}.mp4')
        st.write('**Note**: to download, click on ⋮ and click download')
        st.balloons()
    except Exception as e:
        st.write(e)
