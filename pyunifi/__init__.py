"""
Python __init__ to interact with UniFi Controller
"""
from __future__ import absolute_import
import urllib3
from pyunifi.models.site import Site
from pyunifi.models.siteslist import Siteslist

def http_debug_log_stderr():
    """Dump requests urllib3 debug messages to stderr"""
    urllib3.add_stderr_logger()
