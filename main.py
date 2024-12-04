from environs import Env
import configargparse


def main():
    env = Env()
    env.read_env()


if __name__ == '__main__':
    main()
