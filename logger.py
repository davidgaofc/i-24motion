import os
import csv
import logging
import logstash
import ecs_logging



class Logger:
    """Logs information about our program.
    """

    def __init__(self, name, log_type='FILE', file_path=None, log_level = 'DEBUG'):
        """Constructor of our Logger interface. It sets up a 'custom' logger
        by  setting up the default logging level to INFO, and pointing to the
        file where we'll be appending all the logs.

        Parameters
        ----------
        name : str
            Name of the object instantiating the logger.
        file_path : str
            Path to the logging file.
        """
        self._log_type = log_type.upper()

        if self._log_type == 'FILE':
            # Create a custom logger.
            self._logger = logging.getLogger(name)

            # Create a handler that saves the info to a file.
            file_handler = logging.FileHandler(file_path)

            # Create a formatter and add it to the handler.
            # The format is the following:
            # <DateTime of the log> | <name of object calling the API> | 
            # <message>
            # file_formatter = logging.Formatter(
            #     '%(asctime)s | %(name)s | %(levelname)s | %(message)s ')
            # file_handler.setFormatter(file_formatter)
            file_handler.setFormatter(ecs_logging.StdlibFormatter())

            # Add the handler to our custom logger.
            self._logger.addHandler(file_handler)
        elif self._log_type == 'DB':
            host = 'localhost'
            port = 5000
            self._logger = logging.getLogger('python-logstash-logger')

            self._logger.addHandler(logstash.TCPLogstashHandler(host, port, version=1))
        else:
            raise ValueError(
                f'Unknown log type: {self._log_type}.\n'
                f'Please select one of the following: "FILE", "DB".'
            )

        if(log_level == 'DEBUG'):
            self._logger.setLevel(logging.DEBUG)
        elif(log_level == 'INFO'):
            self._logger.setLevel(logging.INFO)
        elif (log_level == 'WARNING'):
            self._logger.setLevel(logging.WARNING)
        elif (log_level == 'ERROR'):
            self._logger.setLevel(logging.ERROR)
        elif (log_level == 'CRITICAL'):
            self._logger.setLevel(logging.CRITICAL)

    def debug(self, message, extra):
        """Logs the message at the DEBUG level of the `logging` library.

        Parameters
        ----------
        message : str
            The information to be logged.
        """
        self._logger.debug(message, extra=extra)

    def info(self, message, extra):
        """Logs the message at the INFO level of the `logging` library.

        Parameters
        ----------
        message : str
            The information to be logged.
        """
        self._logger.info(message, extra=extra)

    def warning(self, message, extra):
        """Logs the message at the WARNING level of the `logging` library.

        Parameters
        ----------
        message : str
            The information to be logged.
        """
        self._logger.warning(message, extra=extra)

    def error(self, message, extra):
        """Logs the message at the ERROR level of the `logging` library.

        Parameters
        ----------
            message : str
                The information to be logged.
        """
        self._logger.error(message, extra=extra)

    def critical(self, message, extra):
        """Logs the message at the CRITICAL level of the `logging` library.

        Parameters
        ----------
            message : str
                The information to be logged.
        """
        self._logger.critical(message, extra=extra)

