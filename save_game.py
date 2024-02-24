import socket


def save_game(game_state_b: bytes,
              file_path: str = "saved_game.txt"):
    with open(file_path, 'wb') as f:
        f.write(game_state_b)


def load_game(file_path: str = "saved_game.txt"):
    with open(file_path, 'rb') as f:
        game_state_b = f.read()
    return game_state_b


def main():
    HOST = "127.0.0.1"  # local host
    PORT = 61000  # port that server is listening on

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        while True:
            # receive command
            data = s.recv(1024)
            if data.decode() == "save":
                # receive and save data
                data = s.recv(1024)
                save_game(data)
            elif data.decode() == "load":
                # load and send data
                game_state_b = load_game()
                s.sendall(game_state_b)
            elif data.decode() == "close":
                break


if __name__ == "__main__":
    main()
