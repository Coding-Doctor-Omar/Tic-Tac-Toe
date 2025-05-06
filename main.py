from game_brain import Board, Player
from art import logo, options
import os
import time
import sys

def clear_screen():
    """Clears the screen"""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def load_main_menu():
    clear_screen()
    print(logo)
    print(options)

def user_menu_choice():
    return input("Choose an option: ")


def how_to_play():
    clear_screen()
    print(logo)
    print("Type the column letter followed by the row number to place either 'X' or 'O' in the grid, depending on which player you are.")
    print("\nFor example, if you are player 1 and type 'a1' as your move, you place an 'X' on position 'A1' (lower left corner).")
    print("\nIf you decided you want to quit the entire game in the middle of the match, you can type 'quit' as the player move.")
    print("\nIf you want to go back to main menu in the middle of a match, type 'menu' as the player move. Note that this will reset the match status.")
    print("\n\nGood luck, and have fun!")
    input("Press ENTER to go back to main menu.")
    main()

def play_game():
    player_1 = Player(nature="x")
    player_2 = Player(nature="o")
    board = Board()
    current_player = player_1

    while True:
        play_again = None
        clear_screen()
        print(logo)
        board.display()
        if current_player == player_1:
            print("Player X's Turn!\n")
        else:
            print("Player O's Turn!\n")

        player_move = input("Make a move: ").lower()

        if player_move == "quit":
            clear_screen()
            print("Bye!")
            time.sleep(1)
            break

        if player_move == "menu":
            break

        if not hasattr(board, player_move):
            input("Invalid move. For more information, please check the 'How to Play' section.\nTo go back to main menu, type 'menu' as the player move.\nPress ENTER to try again.")
            continue
        else:
            if current_player.play(board, player_move):
                board.refresh_board()
                board.evaluate()

                if board.game_is_over:
                    clear_screen()
                    print(logo)
                    board.display()
                    if board.is_draw:
                        while True:
                            print("It's a draw!\n")
                            play_again = input("Do you want to play again?\nEnter 'y' or 'n': ").lower()

                            if play_again in ["y", "n"]:
                                break
                            else:
                                input("Invalid input. Please enter 'y' or 'n'. Press ENTER to retry.")
                                clear_screen()
                                print(logo)
                                board.display()


                        break
                    else:
                        while True:
                            print(f"Game Over! {board.winner} wins!\n")
                            play_again = input("Do you want to play again?\nEnter 'y' or 'n': ").lower()

                            if play_again in ["y", "n"]:
                                break
                            else:
                                input("Invalid input. Please enter 'y' or 'n'. Press ENTER to retry.")
                                clear_screen()
                                print(logo)
                                board.display()

                        break
            else:
                input("Position already taken! Press ENTER to replay your turn!")
                continue

            if current_player == player_1:
                current_player = player_2
            else:
                current_player = player_1

    if player_move == "menu":
        board.reset_board()
        main()

    if play_again == "y":
        play_game()
    else:
        board.reset_board()
        main()




def main():
    clear_screen()
    load_main_menu()

    user_choice = user_menu_choice()

    if user_choice not in ["1", "2", "3"]:
        input("Invalid option. Please try again. Press ENTER to retry.")
        main()

    if user_choice == "1":
        play_game()

    elif user_choice == "2":
        how_to_play()

    else:
        clear_screen()
        print("Bye!")
        time.sleep(1)
        sys.exit(0)

if __name__ == "__main__":
    main()




