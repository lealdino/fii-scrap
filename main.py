from src.get_fiis import *


def main():
    """Call get_fundos function and print the df to the terminal."""
    df = get_fundos()
    print(df)


if __name__ == '__main__':
    main()
