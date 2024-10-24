
# TODO: accept on upload only mp3 files for now
# TODO: provide ready questions to use which can be removed or edited
# TODO: provide empty prompt to fill in external questions

# TODO: button "Process" which loads and then generates output as a text file
# TODO: also send the output to the email

# TODO: use from Streamlit Dashboard emai/password checker (but put into main side of page not sidebar)

from moviepy.editor import AudioFileClip

# Clip audio
audio = AudioFileClip("data/full_interview.mp3")
cut = audio.subclip(0, 300)  # 300 seconds = 5 minutes
cut.write_audiofile("cut_interview.mp3")