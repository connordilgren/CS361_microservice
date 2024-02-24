import pickle
import socket


def main():
    # game data
    game_state = {"player_1_score": 1,
                  "player_2_score": 2,
                  "board": [
                      ["O", "N", "N"],
                      ["N", "X", "O"],
                      ["X", "X", "X"]
                  ]}

    HOST = "127.0.0.1"  # local host
    PORT = 61000  # listening port

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()

        # send game state to be saved, as bytes object
        game_state_b = pickle.dumps(game_state)
        conn.sendall(b"save")
        conn.sendall(game_state_b)

        # load game state back in
        # note: at most only one game state can be saved
        conn.sendall(b"load")
        data = conn.recv(1024)

        # print loaded data
        game_state_loaded = pickle.loads(data)
        print(game_state_loaded)

        # close microservice
        conn.sendall(b"close")


if __name__ == "__main__":
    main()
