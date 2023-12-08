import os
from sonic_engine.core.engine import Engine

def main():
    file_name = "../config.yaml"
    engine = Engine(os.path.join(__file__, file_name))
    engine.start()

if __name__ == "__main__":
    main()
