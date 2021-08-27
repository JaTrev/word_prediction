from app import page_configuration, introduction, main_body, side_bar, prediction_field

if __name__ == '__main__':
    page_configuration()

    introduction()

    main_body()

    side_bar()

    text = prediction_field()

    print("Text is:")
    print(text)




