from app import page_configuration, introduction, main_body, side_bar, results_field
from word_prediction import load_model, do_predictions


if __name__ == '__main__':
    page_configuration()

    bert_tokenizer, bert_model, distil_tokenizer, distil_model = load_model()

    introduction()

    num_of_predictions, user_input = side_bar()

    main_body(user_input, num_of_predictions)

    if len(user_input):

        bert_words = do_predictions(bert_model, bert_tokenizer, user_input, num_of_predictions)

        distil_words = do_predictions(distil_model, distil_tokenizer, user_input)

        word_dicts = {"bert": bert_words, "distilbert": distil_words}

        results_field(user_input, word_dicts, num_of_predictions)
