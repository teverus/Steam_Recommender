class Action:
    def __init__(
        self,
        name=None,
        function=None,
        arguments=None,
        execute_instantly=False,
        go_back=False,
    ):
        self.name = name
        self.function = function
        self.arguments = arguments
        self.execute_instantly = execute_instantly
        self.go_back = go_back

    def __call__(self, *args, **kwargs):
        if self.arguments:
            self.function(**self.arguments)
        else:
            self.function()
