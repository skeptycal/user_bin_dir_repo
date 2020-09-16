import signal

from subprocess import SubprocessError


class ShellCommandError(SubprocessError):
    """Raised when shell() is called with check=True and the process
    returns a non-zero exit status.

    Attributes:
      cmd, returncode, stdout, stderr, output
    """

    def __init__(self, returncode, cmd, output=None, stderr=None):
        self.returncode = returncode
        self.cmd = cmd
        self.output = output
        self.stderr = stderr

    def __str__(self):
        if self.returncode and self.returncode < 0:
            try:
                return "Command '%s' died with %r." % (
                    self.cmd, signal.Signals(-self.returncode))
            except ValueError:
                return "Command '%s' died with unknown signal %d." % (
                    self.cmd, -self.returncode)
        else:
            return "Command '%s' returned non-zero exit status %d." % (
                self.cmd, self.returncode)

    @property
    def stdout(self):
        """Alias for output attribute, to match stderr"""
        return self.output

    @stdout.setter
    def stdout(self, value):
        # There's no obvious reason to set this, but allow it anyway so
        # .stdout is a transparent alias for .output
        self.output = value


class AnyFileError(Exception):
    """ An error occurred with the AnyFile file. """


class BytesFileError(Exception):
    """ An error occurred with the BytesFile file. """


class TextFileError(Exception):
    """ An error occurred with the TextFile file. """


class TextFileEncodingError(Exception):
    """ An error occurred while encoding the TextFile file. """
