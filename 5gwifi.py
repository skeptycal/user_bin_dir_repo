from typing import Union
from subprocess import CompletedProcess, run, PIPE, STDOUT

# snippet from https://www.programcreek.com/python?code=raw-packet%2Fraw-packet%2Fraw-packet-master%2Fraw_packet%2FUtils%2Fwifi.py


def _support_5ghz(self,
                  wireless_interface: Union[None, str] = None) -> bool:
    # Set wireless interface
    if wireless_interface is None:
        wireless_interface = self._interface

    # Mac OS
    if self._base.get_platform().startswith('Darwin'):
        run([self._airport_path + ' ' + wireless_interface + ' --channel=' +
             str(self._wifi_channels['5 GHz'][0])], shell=True)
        current_channel: CompletedProcess = \
            run([self._airport_path + ' ' + wireless_interface + ' --channel'],
                shell=True, stdout=PIPE, stderr=STDOUT)
        current_channel: str = current_channel.stdout.decode('utf-8')
        if 'channel: ' + str(self._wifi_channels['5 GHz'][0]) in current_channel:
            return True
        else:
            return False

    # Linux
    elif self._base.get_platform().startswith('Linux'):
        available_channels: CompletedProcess = \
            run(['iwlist ' + wireless_interface + ' freq'],
                shell=True, stdout=PIPE, stderr=STDOUT)
        available_channels: str = available_channels.stdout.decode('utf-8')
        if 'Channel ' + str(self._wifi_channels['5 GHz'][0]) in available_channels:
            return True
        else:
            return False

    # Windows
    elif self._base.get_platform().startswith('Windows'):
        return False

    # Other
    else:
        return False
# endregion

# region Switch WiFi channel on interface
