#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    for allnames in dir(hidden_4):
        if not allnames.startswith('__'):
            print("{}".format(allnames))
