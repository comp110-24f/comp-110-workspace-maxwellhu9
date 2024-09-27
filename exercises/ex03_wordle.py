"""EX03 - Wordle - Word Guessing Game"""

__author__ = "730759980"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def input_guess(secret_word_len: int) -> str:
    """Prompt the user to input a guess of the correct length."""
    guess = input(f"Enter a {secret_word_len} character word: ")

    while len(guess) != secret_word_len:
        guess = input(f"That wasn't {secret_word_len} chars! Try again: ")
    return guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Checks if the single character is present in the given word"""
    assert len(char_guess) == 1

    i = 0
    while i < len(secret_word):
        if secret_word[i] == char_guess:
            return True
        i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Return emoji representation of the guess compared to the secret"""
    assert len(guess) == len(secret)

    emoji_result = ""
    i = 0
    while i < len(guess):
        if guess[i] == secret[i]:
            emoji_result += GREEN_BOX
        elif contains_char(secret, guess[i]):
            emoji_result += YELLOW_BOX
        else:
            emoji_result += WHITE_BOX
        i += 1
    return emoji_result


def main(secret: str) -> None:
    """Main game loop"""
    turns = 1
    max_turns = 6

    while turns <= max_turns:
        print(f"=== Turn {turns}/{max_turns} ===")
        guess = input_guess(len(secret))

        print(emojified(guess, secret))

        if guess == secret:
            print(f"You won in {turns}/{max_turns} turns!")
            return
        turns += 1

    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
