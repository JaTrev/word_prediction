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
    st.set_page_config("NLP Language Modeling", layout="centered", initial_sidebar_state="expanded")

    text_chapter = """<style>.chapter {
                        font-size:40px ;} 
                        </style>
                        """
    st.markdown(text_chapter, unsafe_allow_html=True)

    text_subchapter = """
                            <style>.subchapter {
                            font-size:30px ;} 
                            </style>
                            """
    st.markdown(text_subchapter, unsafe_allow_html=True)

    title_font = """
                   <style>.title {
                   font-size:50px ;} 
                   </style>
                   """
    st.markdown(title_font, unsafe_allow_html=True)

    text_font = """
                    <style>.text {
                     } 
                    </style>
                    """

    error_font = """
                        <style>.warning {
                        color: red;} 
                        </style>
                        """
    st.markdown(error_font, unsafe_allow_html=True)
    st.markdown(text_font, unsafe_allow_html=True)

    page_style = """
            <style>
            /* This is to hide hamburger menu completely */
            MainMenu {visibility: hidden;}

            /* This is to hide Streamlit footer */
            footer {visibility: hidden;}
            """
    st.markdown(page_style, unsafe_allow_html=True)


def introduction():

    markdown_text("NLP Word Prediction", TextTypes.Title)

    intro_text = 'Language Modeling (also called Next Word Prediction) is the task of predicting what word comes next '\
                 'and is a fundamental task of NLP. It is used daily when autocompleting a message.'
    markdown_text(intro_text, TextTypes.Text)

    _, col_mid, _ = st.columns([1, 6, 1])

    with col_mid:
        st.markdown(
            f"""
            <div align="center">
                <img src="https://media.arxiv-vanity.com/render-output/5515933/x1.png" width="400">
                <p > Next word prediction is often used when texting. 
                <a href="https://arxiv.org/abs/1811.03604">[Hard, et al., 2018]</a></p>
        
            </div>
            """,
            unsafe_allow_html=True
        )


def main_body(user_input: str, number_of_words: int = 5):
    body_title = 'How this project works'
    markdown_text(body_title, TextTypes.Chapter)

    body_text = f'Start the phrase in the left input field. The following deep learning models will predict ' \
                f'{number_of_words} possible next words.'
    markdown_text(body_text, TextTypes.Text)

    body_text = f'Predicting next word for: '
    markdown_text(body_text, TextTypes.Text)

    st.markdown(
       f"""
                <div align="center">
                
                     {user_input} 
                </div>
                """,
        unsafe_allow_html=True
    )


def get_user_input():
    text = "Type a few words and press enter to get suggestions"
    markdown_text(text, text_class=TextTypes.Subchapter)

    return st.text_input("", max_chars=100, value="Default value")


def side_bar():

    with st.sidebar:

        side_bar_title = "Next Word Prediction"
        markdown_text(side_bar_title, TextTypes.Subchapter)

        side_bar_text = "Number of Predictions"
        num_of_predictions = st.slider(side_bar_text, min_value=1, max_value=7, value=3)

        side_bar_input_text = "Type a few words and press enter."
        user_input = st.text_input(side_bar_input_text, max_chars=100)

    return num_of_predictions, user_input


def results_field(user_input: str, prediction_dict: dict, num_of_predictions: int):
    col1, col2 = st.columns([1, 1])

    with col1:
        markdown_text("Bert", text_class=TextTypes.Chapter)

        for w in prediction_dict["bert"][:num_of_predictions]:

            text = f"""{user_input} <b> {w} </b> """
            markdown_text(text, text_class=TextTypes.Text)

    with col2:
        markdown_text("DistilBert", text_class=TextTypes.Chapter)

        for w in prediction_dict["distilbert"][:num_of_predictions]:
            text = f"""{user_input} <b> {w} </b> """
            markdown_text(text, text_class=TextTypes.Text)
