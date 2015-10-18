import time
import logging
import logging.handlers
from directories import Directories

class ArchiveLogger(object):
    """docstring for ArchiveLogger"""
    def __init__(self):
        self.fh = None
        self.d = Directories()
        self.console_log_level = logging.ERROR
        self.file_log_level = logging.INFO
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(self.d.program_name)
        self.logger.setLevel(logging.DEBUG)
        self.init_console()

    def init_file_logging(self):
        if not self.d.check_myarchive():
            raise Exception, "My Archive Does Not Exist"
        self.fh = logging.FileHandler(self.d.logger)
        self.fh.setLevel(self.file_log_level)
        self.fh.setFormatter(self.formatter)
        self.logger.addHandler(self.fh)
        self.logger.info('\n---------\nLog started on %s.\n---------\n' % time.asctime())

        print "init logger"


    def init_console(self):
        self.ch = logging.StreamHandler()
        self.ch.setLevel(self.console_log_level)
        self.ch.setFormatter(logging.Formatter('%(message)s'))
        self.logger.addHandler(self.ch)

    def print_logger(self):
        self.check_fh()
        if self.d.check_log_exists():
            f = open(self.d.logger)
            s = f.read()
            print s

    def check_fh(self):
        if self.fh is None:
            self.init_file_logging()

    def log_debug(self,msg):
        self.check_fh()
        self.logger.debug(msg)

    def log_info(self,msg):
        self.check_fh()
        print "info"
        self.logger.info(msg)

    def log_error(self,msg):
        self.check_fh()
        self.logger.error(msg)

    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     logging.shutdown([self.d.program_name])
    #     print "shut down"

#=================================================================================
# In APPLICATION CODE, use whichever of the following is appropriate:

# logger.warn('warn message')
# logger.error('error message')
# logger.critical('critical message')

