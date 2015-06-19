# pingchart
Graphical representation of ping.

Sample output:
```
$ pingchart python.org 4                                    
Pinging python.org (104.130.43.121)
█████████ 295 ms
██████████ 314 ms
███████ 237 ms
███████████ 354 ms^C
sent 10 packets
0.00% packet loss
352.50 ms average ping
```

##Installation
Go to the pingchart directory in the terminal and run:
```bash
chmod 755 pingchart.py
ln pingchart.py /usr/local/bin/pingchart
```

##Usage
```bash
pingchart [<url>] [<max lines to display>]
```

By default, pingchart will ping google.com, and it will display enough lines such that a finished command will fill the terminal window.

The chart will display the last \<max lines\> results, but it won't stop pinging when it reaches \<max lines\>, only when quit using ^C.

##Note

This has been tested only on OS X 10.10.4 using zsh.
