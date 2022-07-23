class Action:
    def __init__(self, name=None, function=None, arguments=None, break_after=True):
        self.name = name
        self.function = function
        self.arguments = arguments
        self.break_after = break_after

    def __call__(self, *args, **kwargs):
        if self.arguments:
            self.function(**self.arguments)
        else:
            self.function()
