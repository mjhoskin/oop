import datetime

class Logger():
    '''
    Simple logger - writes to console and to file at three levels of importance.
    
    Attributes
    ----------
    log_file : str
        Location of file to log to
    print_info : bool (optional)
        Whether to print out INFO statements (default True)
    print_warning : bool (optional)
        Whether to print out WARN statements (default True)
    print_error : bool (optional)
        Whether to print out ERROR statements (default True)
        
    Methods
    -------
    info(info_message)
        Prints an Info level message to the console and the log file.
        This is of the form `timestamp INFO: message`
    warn(warning_message)
        Prints a Warning level message to the console and the log file.
        This is of the form `timestamp WARN: message`
    error(error_message)
        Prints an Error level message to the console and the log file.
        This is of the form `timestamp ERROR: message`
    
    Notes
    If print_info, print_warning, and print_error are all set to False, nothing will be logged.
    
    '''
    
    def __init__(self, log_file, 
                 print_info = True,
                 print_warning = True,
                 print_error = True):
        """
        Parameters
        ----------
        log_file : str
            Location of file to log to
        print_info : bool (optional)
            Whether to print out INFO statements (default True)
        print_warning : bool (optional)
            Whether to print out WARN statements (default True)
        print_error : bool (optional)
            Whether to print out ERROR statements (default True)
        """
        
        self._log_file = log_file
        self._print_info = print_info
        self._print_warning = print_warning
        self._print_error = print_error
        
        
    @property
    def log_file(self):
        return self._log_file
    
    @log_file.setter
    def log_file(self, value):
        if isinstance(value, str):
            self._log_file = value
        else:
            raise ValueError('log_file must be a string')
    
    @property
    def print_info(self):
        return self._print_info
    
    @print_info.setter
    def print_info(self, value):
        if isinstance(value, bool):
            self._print_info = value
        else:
            raise ValueError('print_info must be a boolean')
                   
    @property
    def print_warning(self):
        return self._print_warning
    
    @print_warning.setter
    def print_warning(self, value):
        if isinstance(value, bool):
            self._print_warning = value
        else:
            raise ValueError('print_warning must be a boolean')
            
    @property
    def print_error(self):
        return self._print_error
    
    @print_error.setter
    def print_error(self, value):
        if isinstance(value, bool):
            self._print_error = value
        else:
            raise ValueError('print_error must be a boolean')
    
    def __str__(self):
        """
        Returns a high level description of the object. 
        """
        
        return "A logger object, used to write messages to console and file, of different levels of importance"

    def __repr__(self):
        """
        Returns a string that can be used to recreate the object. 
        """
        
        return "{0}('{1}',{2},{3},{4})".format(self.__class__.__name__,
                                             self.log_file,
                                             self.print_info,
                                             self.print_warning,
                                             self.print_error)
                
    def info(self, info_message):
        """Logs an info level message. If print_info is False, has no effect.
        
        Parameters 
        ----------
        info_message : str
            The message to log
        """
        
        if self._print_info:
            #generate full message
            full_info = "{0} INFO: {1}\n".format(datetime.datetime.now(), info_message)
            
            #print to console
            print(full_info)
            
            #print to log file
            with open(self.log_file, mode = 'a') as f:
                f.write(full_info)
            
    def warning(self, warning_message):
        """Logs a warning level message. If print_warning is False, has no effect.
        
        Parameters 
        ----------
        warning_message : str
            The message to log
        """
        if self._print_warning:
            #generate full message
            full_warning = "{0} WARNING: {1}\n".format(datetime.datetime.now(), warning_message)
            
            #print to console
            print(full_warning)
            
            #print to log file
            with open(self.log_file, mode = 'a') as f:
                f.write(full_warning)
                
    def error(self, error_message):
        """Logs an error level message. If print_error is False, has no effect.
        
        Parameters 
        ----------
        error_message : str
            The message to log
        """
        
        if self._print_error:
            #generate full message
            full_error = "{0} ERROR: {1}\n".format(datetime.datetime.now(), error_message)
            
            #print to console
            print(full_error)
            
            #print to log file
            with open(self.log_file, mode = 'a') as f:
                f.write(full_error)
            
            
log = Logger('log.txt')

log.error('Here is an error message! Something catastrophic has occurred!')
log.warning('Here is a warning message. Something strange is happening, that you should be aware of.')
log.info('Here is an informative message. Processing has reached a certain point.')
