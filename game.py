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
        save_params = {"command": "save",
                       "game_state": game_state,
                       "file": "game_1.txt"}
        save_params_b = pickle.dumps(save_params)
        conn.sendall(save_params_b)

        # load game state back in
        load_params = {"command": "load",
                       "file": "game_1.txt"}
        load_params_b = pickle.dumps(load_params)
        conn.sendall(load_params_b)
        game_state_b = conn.recv(1024)

        # print loaded data
        game_state = pickle.loads(game_state_b)
        print(game_state)

        # close microservice
        close_params = {"command": "close"}
        close_params_b = pickle.dumps(close_params)
        conn.sendall(close_params_b)


if __name__ == "__main__":
    main()
