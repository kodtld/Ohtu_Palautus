from tennis_game import TennisGame


def main():
    game = TennisGame("player1", "player2")

    print(game.get_score())

    game.won_point("home")
    print(game.get_score())

    game.won_point("away")
    print(game.get_score())

    game.won_point("away")
    print(game.get_score())

    game.won_point("home")
    print(game.get_score())

    game.won_point("away")
    print(game.get_score())

    game.won_point("home")
    print(game.get_score())

    game.won_point("home")
    print(game.get_score())

    game.won_point("away")
    print(game.get_score())

    game.won_point("home")
    print(game.get_score())

if __name__ == "__main__":
    main()
