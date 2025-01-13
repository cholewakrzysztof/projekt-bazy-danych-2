import datetime
import string


class LoggedUserContext:
# Static attribute to store the connection string

    ADMIN_CONNECTION = 'admin'
    WORKER_CONNECTION = 'worker'
    CLIENT_CONNECTION = 'client'
    DEFAULT_CONNECTION = 'default'

    connection_string = DEFAULT_CONNECTION
    expires_date = datetime.date.today()

    @staticmethod
    def get_connection_string():
        # Static method to return the connection string
        return LoggedUserContext.connection_string

    @staticmethod
    def setup_logged_context(exp_date: datetime, user_type: string):
        LoggedUserContext.expires_date = exp_date
        if user_type == LoggedUserContext.ADMIN_CONNECTION:
            LoggedUserContext.connection_string = LoggedUserContext.ADMIN_CONNECTION
        elif user_type == LoggedUserContext.WORKER_CONNECTION:
            LoggedUserContext.connection_string = LoggedUserContext.WORKER_CONNECTION
        elif user_type == LoggedUserContext.CLIENT_CONNECTION:
            LoggedUserContext.connection_string = LoggedUserContext.CLIENT_CONNECTION