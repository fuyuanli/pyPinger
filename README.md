pyPinger
===

## Requirement

```python3=
$ virtualenv -p python3 env
$ source env/bin/activate
$ pip3 install -r ./requirements.txt
```

## Usage

```python3
from pyPinger import * 
myHost = pyPinger("www.google.com.tw", 10) # ping www.google.com.tw -c10
myHost.process()
```

## Output
```bash=
[Message] Pinging www.google.com.tw ...
[12.1, 12.0, 12.0, 12.0, 12.0, 12.0, 12.1, 12.0, 11.9, 12.0]
```
![](../www.google.com.tw.png)
