#!/usr/bin/env python3

from core.jdbc import Jdbc

def main():
    res = Jdbc().query("show tables")
    print(res)


if __name__ == '__main__':
    main()

