from app import response_functions

# Start server when `python main.py` is run
if __name__ == "__main__":
    from server import run_server

    run_server({"info": response_functions.info, "start": response_functions.start, "move": response_functions.move, "end": response_functions.end})