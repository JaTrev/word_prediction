from transformers import BertTokenizer, BertForMaskedLM, DistilBertTokenizer, DistilBertForMaskedLM
import torch
import string
import streamlit as st


@st.cache
def load_model():
    """
    load_model loads the tokenizer and model

    :return:
    """

    model_name = "bert-base-uncased"
    bert_tokenizer = BertTokenizer.from_pretrained(model_name)
    bert_model = BertForMaskedLM.from_pretrained(model_name).eval()

    model_name = "distilbert-base-uncased"
    distil_tokenizer = DistilBertTokenizer.from_pretrained(model_name)
    distil_model = DistilBertForMaskedLM.from_pretrained(model_name).eval()

    return bert_tokenizer, bert_model, distil_tokenizer, distil_model


@st.cache
def decode(tokenizer, pred_idxs):
    """
    decode is used to translate the translate the ids to tokens

    :param tokenizer: tokenizer used for encoding/decoding
    :param pred_idxs: list of indices
    :return:
    """

    ignore_tokens = string.punctuation + '[PAD]'
    tokens = []
    for w in pred_idxs:
        token = ''.join(tokenizer.decode(w).split())
        if token not in ignore_tokens:
            tokens.append(token.replace('##', ''))
    return tokens


@st.cache
def encode(tokenizer, text_sentence, add_special_tokens=True):
    """
    encode is uses to translate the input into indices

    :param tokenizer: tokenizer used for encoding/decoding
    :param text_sentence: text to transfrom
    :param add_special_tokens:  flag for special token

    :return:
    """
    text_sentence = text_sentence.replace('<mask>', tokenizer.mask_token)

    # if <mask> is the last token, append a "." so that models dont predict punctuation.
    if tokenizer.mask_token == text_sentence.split()[-1]:
        text_sentence += ' .'

    input_ids = torch.tensor([tokenizer.encode(text_sentence, add_special_tokens=add_special_tokens)])
    mask_idx = torch.where(input_ids == tokenizer.mask_token_id)[1].tolist()[0]
    return input_ids, mask_idx


@st.cache(allow_output_mutation=True)
def do_predictions(model, tokenizer, text_sentence, max_top_k_words=10):
    """
    do_predictions predicts the next word for the input sentence
    :param model: transformer model
    :param tokenizer: tokenizer used for encoding and decoding
    :param text_sentence: input sentence on which the prediction is based
    :return:
    """

    text_sentence = "Hello my"
    text_sentence += ' <mask>'

    # input_ids, mask_idx = encode(tokenizer, text_sentence)

    # with torch.no_grad():
    #     predict = model(input_ids)[0]

    # words = decode(tokenizer, predict[0, mask_idx, :].topk(max_top_k_words).indices.tolist())

    return ["this", "is", "a", "test"]
