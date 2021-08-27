import streamlit as st
from enum import Enum


class TextTypes(Enum):
    Text = "text"
    Chapter = "chapter"
    Subchapter = "subchapter"
    Warning = "warning"
    Title = "title"


def markdown_text(text: str, text_class: TextTypes = TextTypes.Text):
    """
    markdown_text is used to create text on the streamlit page

    :param text: string that should appear on the page
    :param text_class: type of text presentation
    :return:
    """
    assert text_class in TextTypes

    st.markdown(f'<p class="{text_class.value}"> {text} </p>', unsafe_allow_html=True)


def page_configuration():
    st.set_page_config("NLP Word Prediction", layout="centered", initial_sidebar_state="expanded")

    text_chapter = """<style>.chapter {
                        font-size:40px ;font-family: 'Cooper Black'; color: grey;} 
                        </style>
                        """
    st.markdown(text_chapter, unsafe_allow_html=True)

    text_subchapter = """
                            <style>.subchapter {
                            font-size:30px ;font-family: 'Cooper Black'; color: grey;} 
                            </style>
                            """
    st.markdown(text_subchapter, unsafe_allow_html=True)

    title_font = """
                   <style>.title {
                   font-size:50px ; font-family: 'Cooper Black'; color: #FF9633;} 
                   </style>
                   """
    st.markdown(title_font, unsafe_allow_html=True)

    text_font = """
                    <style>.text {
                     font-family: 'Cooper Black'; color: black;} 
                    </style>
                    """

    error_font = """
                        <style>.warning {
                         font-family: 'Cooper Black'; color: red;} 
                        </style>
                        """
    st.markdown(error_font, unsafe_allow_html=True)
    st.markdown(text_font, unsafe_allow_html=True)

    page_style = """
            <style>
            /* This is to hide hamburger menu completely */
            #MainMenu {visibility: hidden;}

            /* This is to hide Streamlit footer */
            footer {visibility: hidden;}
            """
    st.markdown(page_style, unsafe_allow_html=True)


def introduction():

    markdown_text("NLP Word Prediction", TextTypes.Title)

    intro_text = 'This project looks at the word prediction task of NLP.'
    markdown_text(intro_text, TextTypes.Text)

    # todo: missing a picture


def main_body():
    body_title = 'Main Body Title'
    markdown_text(body_title, TextTypes.Chapter)

    body_text = 'reason for the project and intro to word intrusion task'
    markdown_text(body_text, TextTypes.Text)


def prediction_field():
    text = "Type a few words and press enter to get suggestions"
    markdown_text(text, text_class=TextTypes.Subchapter)

    return st.text_input("", max_chars=100)


def side_bar():

    with st.sidebar:

        side_bar_text = "Number of Predictions"
        markdown_text(side_bar_text, TextTypes.Subchapter)

        num_of_predictions = st.slider("", min_value=1, max_value=7)

    return num_of_predictions






