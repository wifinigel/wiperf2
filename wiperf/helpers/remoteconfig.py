"""
Functions to retrieve centralized remote config file

TODO: Convert to object
"""

import warnings
import requests
from requests.exceptions import HTTPError
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import time

####################################
# config server
####################################
def anon_value(value):
    """
    Turn value in to anonymous value to protect sensitve data that will 
    be printed in log info 

    Args:
        value (string): value to be anonymised
    
    Return:
        Anonymised string
    """
    value = str(value)

    if len(value) < 4:
        return len(value) * "*"
    else:
        return value[0] + (len(value) -2) * "*" + value[-1]

def read_remote_cfg(config_file, check_cfg_file, config_vars, file_logger):
    """
    Pull the remote cfg file if refresh time expired or on first boot
    """

    cfg_file_url = config_vars['cfg_url']
    cfg_token = config_vars['cfg_token']
    cfg_username = config_vars['cfg_username']
    cfg_password = config_vars['cfg_password']
    cfg_text = ''
    
    file_logger.debug("Trying to pull config file from URL: {}".format(cfg_file_url))

    # if we use a token, we need to set user/pwd to be token
    if cfg_token:
        cfg_username = cfg_token
        cfg_password = cfg_token
        file_logger.debug("Credential used (token): {}".format(anon_value(cfg_token)))
    else:
        file_logger.debug("Credential used (user/pwd): {} / {}".format(anon_value(cfg_username), anon_value(cfg_password)))

    try:
        warnings.simplefilter('ignore',InsecureRequestWarning)
        response = requests.get(cfg_file_url, auth=(cfg_username, cfg_password), timeout=5)
        if response.status_code == 200:
            cfg_text = response.text
            file_logger.debug("HTTP reponse code: {}".format(response.status_code))
            file_logger.info("Config file pulled OK.")
        else:
            file_logger.error("Config file pull failed: {} ({}) - Note: Pretty much everything fails as a 404 on GitHub (if that is your remote target), even auth issues".format(response.status_code, response.text))
            return False
    except Exception as err:
        file_logger.error("Config file pull error:")
        file_logger.error("HTTP get error: {}".format(err))
        return False

    if cfg_text:
        file_logger.info("Writing pulled config file to local config...")
        try:   
            with open(config_file, 'w') as f:
                f.write(cfg_text)
            file_logger.info("Local config file written OK.")
            write_cfg_timestamp(check_cfg_file, file_logger)
            return True
        except Exception as ex:
            file_logger.error("Config file write error:")
            file_logger.error("Issue writing cfg timestamp file: {}".format(ex))
            return False
    else:
        file_logger.info("No data detected in cfg file, nothing written to file (check file URL)")
        return False

def write_cfg_timestamp(check_cfg_file, file_logger):
    """
    Write current timestamp to cfg timestamp file
    """
    
    time_now = str(int(time.time()))
    
    file_logger.info("Writing current time to cfg timestamp file...")
    try:   
        with open(check_cfg_file, 'w') as f:
            f.write(time_now)
        file_logger.info("Written OK.")
        return True
    except Exception as ex:
        file_logger.error("Issue writing cfg timestamp file: {}".format(ex))
        return False


def check_last_cfg_read(config_file, check_cfg_file, config_vars, file_logger):
    """
    Read timestamp from cfg timestamp file and force pull of remote cfg file if required
    """

    time_now = int(time.time())
    last_read_time = 0

    file_logger.info("Checking cfg last-read timestamp...")
    try:
        with open(check_cfg_file) as f:
            last_read_time = f.read()
        file_logger.debug("Last read timestamp: {}".format(last_read_time))
    except FileNotFoundError:
        # file does not exist
        file_logger.info("Timestamp file does not exist yet - will be created after successful read from remote file store.")
    except Exception as e:
        file_logger.info("File read error: {}".format(e))
        return False
    
    # if config file not read in last refresh interval, pull cfg file
    file_logger.debug("Checking time diff, time now: {}, last read time: {}".format(time_now, last_read_time))

    cfg_refresh_interval = int(config_vars['cfg_refresh_interval'])
    if (time_now - int(last_read_time)) >  cfg_refresh_interval:
        file_logger.info("Time to read remote cfg file...")
        return read_remote_cfg(config_file, check_cfg_file, config_vars, file_logger)
    else:
        file_logger.info("Not time to read remote cfg file.")
        return False
