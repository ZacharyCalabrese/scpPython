# scpPython

### Usage

Copy a file from a local machine to a remote machine
```Python
from scpPythonConnector import send_file

send_file('FILE.ext', 'DESTINATION / File.ext', 'username@hostaddress', PORT)
```

Copy a file from a remote machine to a local machine
```Python
from scpPythonConnector import get_file

get_file('SOURCE PATH / File.ext', 'username@hostaddress', PORT)
```
