#!/usr/bin/env python3
from freqtrade_client import __version__ as client_version

from freqtrade import __version__ as ft_version


def main():
    if ft_version != client_version:
        print(f"Versions do not match: \n"
              f"ft: {ft_version} \n"
              f"client: {client_version}")
        exit(1)
    print(f"Versions match: ft: {ft_version}, client: {client_version}")
    exit(0)


if __name__ == '__main__':
    main()
