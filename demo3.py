import fire


class Calculator(object):
    """A simple calculator class."""

    def __init__(self, name):
        self.name = name
    
    def double(self, number):
        return 2 * number


if __name__ == '__main__':
    fire.Fire(Calculator)
