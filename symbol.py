import argparse


class Config:
    args = None

    def __init__(self):
        parser = argparse.ArgumentParser(description='Secret value descriptor')
        parser.add_argument('--secret', '-s', dest='secret_value', help='Secret value')
        self.args = parser.parse_args()


cfg = Config()


for symbol in cfg.args.secret_value:
    print(symbol)
