# Import
import threading

# Import Files
from src.render import render


def main():
    render_thread = threading.Thread(target=render)
    render_thread.start()
    print("\noi")

if (__name__ == "__main__"):
    main()