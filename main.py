from app import page_configuration, introduction, main_body, side_bar, results_field, get_user_input
from word_prediction import load_model, do_predictions

if __name__ == '__main__':
    page_configuration()

    tokenizer, model = load_model("bert")

    introduction()

    num_of_predictions, user_input = side_bar()

    main_body(num_of_predictions)

    if user_input:

        top_prediction_words = do_predictions(model, tokenizer, user_input, num_of_predictions)

        results_field(top_prediction_words)
