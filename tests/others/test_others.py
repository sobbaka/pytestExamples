from src.enums.global_enums import GlobalErrorMessage

def test_others_say_hello(say_hello):
    assert say_hello == 14, GlobalErrorMessage.WRONG_NUMBER.value
