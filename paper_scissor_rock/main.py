import pytest
# user_option= input ('piedra, papel, tijera=>')
# computer_option='piedra'

# if user_option==computer_option:
#   print('empate!!!')
# # elif user_option=='piedra':
# #   if computer_option=='tijera':
# #     print('piedra gana a tijera')
# #     print('user gano')
# #   else:
# #     print('papel gana a piedra')
# #     print('computer gano')
# elif user_option == 'papel':
#   if computer_option=='piedra':
#     print('papel gana a piedra')
#     print('user gano!')
#   else:
#     print('tijera gana apapel')
#     print('computer gano')
# elif user_option=='tijera':
#   if computer_option=='papel':
#     print('tijera gana a papel')
#     print('user gano')
#   else:
#     print('piedra gana tijera')
#     print('computer gano')


# input 

# 3 opciones : [piedra, papel, tijera]

# output 

# 3 opciones: ganar, perder, empate

def generate_computer_option():
    # rock, paper, scissor, random.random choice

    result = ""
    return result



def compare_options(user_option: str, computer_option: str) -> str:

    if user_option == computer_option:
        return "tie"
    elif user_option == "scissor" and computer_option == "paper":   
        return "win"
    elif user_option == "scissor" and computer_option == "rock":
        return "lose"
    elif user_option == "paper":
        if computer_option == "scissor":
            return "lose"
        elif computer_option == "rock":
            return "win"
    elif user_option == "rock" and computer_option == "paper":   
        return "lose"
    elif user_option == "rock" and computer_option == "scissor":   
        return "win"
    else:
        raise NameError

def main():
    user_option = input()
    computer_option = generate_computer_option()

    result = compare_options(user_option, computer_option)

    print(f"user {result}")



