from main import compare_options

def test_compare_options_rock():
    assert compare_options("rock", "rock") == "tie"

def test_compare_options_paper():
    assert compare_options("paper", "paper") == "tie"

def test_compare_options_scissor():
    assert compare_options("scissor", "scissor") == "tie"

def test_compare_options_scissor_rock():
    assert compare_options("scissor", "rock") == "lose"

def test_compare_options_scissor_papaer():
    assert compare_options("scissor", "paper") == "win"

def test_compare_options_paper_rock():
    assert compare_options("paper", "rock") == "win"

def test_compare_options_paper_scissor():
    assert compare_options("paper", "scissor") == "lose"

def test_compare_options_rock_scissor():
    assert compare_options("rock", "scissor") == "win"

def test_compare_options_rock_paper():
    assert compare_options("rock", "paper") == "lose"












