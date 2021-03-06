import streamlit as st
import my_functions
from my_functions import *

def main():
	st.title('Transpose streamlit app')

	layout = st.sidebar.container()
	with layout:
		transpose_down = st.button('b')
		transpose_up = st.button('#')

	myform = st.form(key='text')
	with myform:
		text = st.text_area('Lyrics + chords, chords should be in [ ]')
		submit = st.form_submit_button(label='Submit')

	if submit:
		st.session_state.song = text.replace('\n', '\n\n')
		st.write(st.session_state.song)

	if transpose_down:
		st.session_state.song = transpose_song(st.session_state.song, -1)
		st.write(st.session_state.song)

	if transpose_up:
		st.session_state.song = transpose_song(st.session_state.song, 1)
		st.write(st.session_state.song)

if __name__ == '__main__':
    main()
