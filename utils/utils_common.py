import os
import errno
import ntpath


def mkdir_p(path):
    """ mkdir -p
    """
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


def remove_files_keeping_encode(temp_folder, encoded_file):
    """ remove files but keep encode
    """
    for f in listdir_full_path(temp_folder):
        if ntpath.basename(f) != ntpath.basename(encoded_file):
            os.remove(f)


def listdir_full_path(directory):
    """ like os.listdir(), but returns full absolute paths
    """
    for f in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, f)):
            yield os.path.abspath(os.path.join(directory, f))


def decode(value):
    """ Convert bytes to string, if needed
    """
    if isinstance(value, bytes):
        return value.decode("utf-8")
    return value


def run_program_simple(*args, **kwargs):
    """ simple way to run a command ignoring stderr and stdout
    """
    output = os.system(" ".join(*args) + " >/dev/null 2>&1", **kwargs)
    if output != 0:
        raise RuntimeError("failed to execute " + " ".join(*args))


def get_filename_with_temp_folder(temp_folder, filename):
    """ helper to get filename with temp folder
    """
    return os.path.join(temp_folder, filename)


if __name__ == '__main__':
    pass