#!/usr/bin/python3
""" Fabfile that generates a .tgz archive from the contents of web_static
using the function do_pack
"""
from datetime import datetime
from fabric import operations


def do_pack():
    """ The do_pack function that generates the .tgz archive"""
    # Create versions dir if it doesn't exist
    operations.local("mkdir -p versions")

    # format of file to be made:
    # web_static_<year><month><day><hour><minute><second>.tgz
    format1 = "%Y%m%d%H%M%S"
    file_time = datetime.utcnow().strftime(format1)
    filename = "web_static_"
    filename += file_time
    filename += ".tgz"

    # Create the .tgz archive
    result = operations.local(
            "tar -cvzf 'versions/{}' web_static".
            format(filename))

    # If archive was made, return. Otherwise , return None
    if result is not None:
        return result
    else:
        return None
