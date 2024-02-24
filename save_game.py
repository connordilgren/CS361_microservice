import pickle
import socket


def main():
    HOST = "127.0.0.1"  # local host
    PORT = 61000  # port that server is listening on

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        while True:
            # receive and unpickle command
            data_b = s.recv(1024)
            data = pickle.loads(data_b)

            if data["command"] == "save":
                # receive and save data
                game_state = data["game_state"]
                file = data["file"]
                with open(file, 'wb') as f:
                    pickle.dump(game_state, f)

            elif data["command"] == "load":
                # load and send data
                file = data["file"]
                with open(file, 'rb') as f:
                    game_state = pickle.load(f)
                game_state_b = pickle.dumps(game_state)
                s.sendall(game_state_b)

            elif data["command"] == "close":
                break


if __name__ == "__main__":
    main()
