def grammar_check(text_check):
    if (text_check[0].isupper() and text_check[-1] in '!.?"') == True:
        return True
    elif (text_check[0].isupper() and text_check[-1] not in '!.?"'):
        return "Check punctuation"
    elif (text_check[0].islower() and text_check[-1] in '!.?"'):
        return "Check capital letter"
    elif (text_check[0].islower() and text_check[-1] not in '!.?"'):
        return "Check capital letter and punctuation"