#!/usr/bin/env python3

from ._util import *
from ._util import _debug_
# from ._util import BasicColors, Popen, Union, AnyStr, List


bc = BasicColors()


@dataclass
class Shell(Popen):
    platform: str = sys.platform.lower
    cwd: PathLike = Path().cwd

    # TODO - ... snippets from python 3.8.5
    # @property
    # def universal_newlines(self):
    #     # universal_newlines as retained as an alias of text_mode for API
    #     # compatibility. bpo-31756
    #     return self.text_mode

    # @universal_newlines.setter
    # def universal_newlines(self, universal_newlines):
    #     self.text_mode = bool(universal_newlines)

    # def _translate_newlines(self, data, encoding, errors):
    #     data = data.decode(encoding, errors)
    #     return data.replace("\r\n", "\n").replace("\r", "\n")

    # def __enter__(self):
    #     return self

    # def __exit__(self, exc_type, value, traceback):
    #     if self.stdout:
    #         self.stdout.close()
    #     if self.stderr:
    #         self.stderr.close()
    #     try:  # Flushing a BufferedWriter may raise an error
    #         if self.stdin:
    #             self.stdin.close()
    #     finally:
    #         if exc_type == KeyboardInterrupt:
    #             # https://bugs.python.org/issue25942
    #             # In the case of a KeyboardInterrupt we assume the SIGINT
    #             # was also already sent to our child processes.  We can't
    #             # block indefinitely as that is not user friendly.
    #             # If we have not already waited a brief amount of time in
    #             # an interrupted .wait() or .communicate() call, do so here
    #             # for consistency.
    #             if self._sigint_wait_secs > 0:
    #                 try:
    #                     self._wait(timeout=self._sigint_wait_secs)
    #                 except TimeoutExpired:
    #                     pass
    #             self._sigint_wait_secs = 0  # Note that this has been done.
    #             return  # resume the KeyboardInterrupt

    #         # Wait for the process to terminate, to avoid zombies.
    #         self.wait()

    # def __del__(self, _maxsize=sys.maxsize, _warn=warnings.warn):
    #     if not self._child_created:
    #         # We didn't get to successfully create a child process.
    #         return
    #     if self.returncode is None:
    #         # Not reading subprocess exit status creates a zombie process which
    #         # is only destroyed at the parent python process exit
    #         _warn("subprocess %s is still running" % self.pid,
    #               ResourceWarning, source=self)
    #     # In case the child hasn't been waited on, check if it's done.
    #     self._internal_poll(_deadstate=_maxsize)
    #     if self.returncode is None and _active is not None:
    #         # Child is still running, keep us alive until we can wait on it.
    #         _active.append(self)


def shell(args: Union[AnyStr, List[AnyStr]],
          input: AnyStr = None,
          capture_output: bool = True,
          timeout: float = DEFAULT_TIMEOUT,
          check: bool = True,
          ignore_errors: bool = True,
          encoding: str = DEFAULT_ENCODING,
          debug: bool = _debug_,
          env: Dict = {},
          **kwargs) -> CompletedProcess:
    """ #### Run a shell command using and return a CompletedProcess Instance

        Params:
        - args - shell command and arguments
        - input - optional `stdin` str or bytes
        - timeout - optional time limit to wait for response
        - check - check returncode for non-zero and raise an exception
        - ignore_errors - ignore errors and return whatever is available
        - verbose - catch and return output details
        - env - environment mapping

        Return:
        - args, stdout, stderr
        - returncode - shell command return code (0 is success)

        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


        Reference: Docs for subprocess.run (python 3.8.5)

        Use subprocess.run to access command line results.

        Run command with arguments and return a CompletedProcess instance.

        The returned instance will have attributes args, returncode, stdout and
        stderr. By default, stdout and stderr are not captured, and those
        attributes will be None. Pass stdout=PIPE and/or stderr=PIPE in order to
        capture them.

        If check is True and the exit code was non-zero, it raises a
        CalledProcessError. The CalledProcessError object will have the return
        code in the returncode attribute, and output & stderr attributes if
        those streams were captured.

        If timeout is given, and the process takes too long, a TimeoutExpired
        exception will be raised.

        There is an optional argument "input", allowing you to pass bytes or a
        string to the subprocess's stdin. If you use this argument you may not
        also use the Popen constructor's "stdin" argument, as it will be used
        internally.

        By default, all communication is in bytes, and therefore any "input"
        should be bytes, and the stdout and stderr will be bytes. If in text
        mode, any "input" should be a string, and stdout and stderr will be
        strings decoded according to locale encoding, or by "encoding" if set.
        Text mode is triggered by setting any of text, encoding, errors or
        universal_newlines.

        The other arguments are the same as for the Popen constructor.
        """

    if not args:
        raise ShellCommandError(
            f"The 'shell' command requires some arguments. None were provided.")
    # join sequences into strings and bytes
    if isinstance(args, (tuple, set, list)):
        if isinstance(args[0], str):
            args = tuple(' '.join(args).split())
            # args = args.encode(encoding) if not WIN32 else args
        if isinstance(args[0], bytes):
            args = tuple(b' '.join(args).split())
    elif not isinstance(args, (str, bytes)):
        raise TypeError(f'Arguments must be str or bytes, not {type(args)}')

    args = args.split()

    # stdout = PIPE if verbose else None
    # stderr = PIPE if verbose else None  # or STDOUT

    # timeout guard
    if timeout and not isinstance(timeout, float):
        try:
            timeout = float(timeout)
        except (NameError, OverflowError, TypeError, ValueError, ZeroDivisionError) as e:
            # if the problem was an invalid format or type for the timeout, use
            # the default timeout value
            if ignore_errors:
                timeout = DEFAULT_TIMEOUT
            raise
        except Exception as e:
            # all other errors return an error
            if ignore_errors:
                return e
            raise

    try:
        # The returned CompletedProcess instance will have:
        # args, returncode, stdout, and stderr.
        # "input" is optionally used to pass bytes or string to stdin,
        # but is mutually exclusive with Popen's "stdin"
        return run(args=args, capture_output=capture_output,  input=input, encoding=encoding, timeout=timeout, check=check)
    except CalledProcessError as e:
        # An actual error returned from the invoked command 'args'
        # The CalledProcessError instance will have:
        # returncode attribute, and output & stderr if captured.
        if ignore_errors:
            return e  # TODO - log and improve error message
        raise
    except TimeoutError as e:
        # Frozen? Or a long running command was not given enough time to
        # complete. If timeout is given, and the process takes too long,
        # a TimeoutExpired exception will be raised.
        if ignore_errors:
            return e  # TODO - log and improve error message
        raise
    except (FileNotFoundError, IOError, OSError) as e:
        # An actual OSError is caught. We cannot be sure what
        # information is available.
        if ignore_errors:
            return e  # TODO - log and improve error message
        raise
    except (TypeError, ValueError) as e:
        # parameters incorrect type?
        if ignore_errors:
            return e  # TODO - log and improve error message
        raise
    except Exception as e:
        # something very strange happened!
        if ignore_errors:
            return e  # TODO - log and improve error message
        raise


def repl(args: str = '', debug: int = 0) -> CompletedProcess:
    try:
        retval = shell(args=args, ignore_errors=True,
                       capture_output=True, debug=_debug_)
    except Exception as e:
        print('Error: ', e)
        return

    if retval.returncode:
        print(f'{bc.LIME}Return Code: {bc.ATTN}{retval.returncode}{bc.RESET}')
        print(f'{retval.stderr}')
    else:
        print(retval.stdout)
    return retval


def ls(filenames: str = '', params: str = '--group-directories-first --color=tty -ghlAG ') -> str:
    args = f'ls {filenames.strip()} {params.strip()}'
    retval = repl(args)
    if retval.returncode:
        if retval.stderr:
            return retval.stderr

    return retval


def check(args: str):
    return shell(args=args, verbose=False).returncode


if __name__ == '__main__':
    test_cmd: str = 'ls -lAhF'
    print(shell(test_cmd))
