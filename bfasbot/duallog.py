
# Import required standard packages.
import datetime
import logging.handlers
import os, pyrogram


def setup(logdir='log'):
    # Create the root logger.
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    # Validate the given directory.
    logdir = os.path.normpath(logdir)

    # Create a folder for the logfiles.
    if not os.path.exists(logdir):
        os.makedirs(logdir)

    # Construct the logfile name.
    t = datetime.datetime.now()
    logfile = '{year:04d}{mon:02d}{day:02d}-' \
        '{hour:02d}{min:02d}{sec:02d}.log'.format(
            year=t.year, mon=t.month, day=t.day, 
            hour=t.hour, min=t.minute, sec=t.second)
    logfile = os.path.join(logdir, logfile)

    # Set up logging to the logfile.
    filehandler = logging.handlers.RotatingFileHandler(
        filename=logfile,
        maxBytes=10*1024*1024,
        backupCount=100)
    filehandler.setLevel(logging.DEBUG)
    fileformatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    filehandler.setFormatter(fileformatter)
    logger.addHandler(filehandler)
     
    # Set up logging to the console.
    streamhandler = logging.StreamHandler()
    streamhandler.setLevel(logging.WARNING)
    streamformatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    streamhandler.setFormatter(streamformatter)
    logger.addHandler(streamhandler)


if __name__ == '__main__':
    """Illustrate the usage of the duallog package.
    """

    # Set up dual logging.
    logdir = 'log'
    setup(logdir)