class Logger:
    """
    A simple logger class that logs messages with a specified log level.

    Attributes:
        log_level (str): The log level for messages logged by this Logger instance.

    Methods:
        __init__: Initializes a new Logger instance with a specified log level.
        __call__: Logs a message with the instance's log level.
    """
    def __init__(self, log_level: str) -> None:
        """
        Initializes a new Logger instance with the given log level.
        :param log_level:
        """
        self.log_level = log_level

    def __call__(self, message: str) -> str:
        """
        Logs a message with the instance's log level.
        :param message:
        :return:
        """
        return f"{self.log_level}: {message}"
