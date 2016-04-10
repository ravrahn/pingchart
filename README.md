# pingchart
Graphical representation of ping.

Sample output:
<pre>
Pinging <b>python.org</b> (104.130.43.121)
███████ 237 ms
█████████ 348 ms
██████████ 368 ms
██████████ 388 ms^C
<b>10</b> packets sent, <b>10</b> packets received
<b>0.00%</b> packet loss
<b>307.80</b> ms average ping
<b>233</b> ms lowest, <b>419</b> ms highest
</pre>

##Installation
Go to the pingchart directory in the terminal and run:
```bash
chmod 755 pingchart.py
ln pingchart.py /usr/local/bin/pingchart
```

###Dependancies
pingchart requires Python 3 and uses the `sh` and `blessings` libraries, both available on pip. It also requires the `dig` command, which is often preinstalled. If not, it is available in the package `dnsutils` on apt.

##Usage
```bash
pingchart [<url>] [<max lines to display>]
```

By default, pingchart will ping google.com, and it will display enough lines such that a finished command will fill the terminal window.

The chart will display the last \<max lines\> results, but it won't stop pinging when it reaches \<max lines\>, only when quit using ^C.

##Notes

* This has been tested on OS X 10.10 with iTerm and Terminal, running zsh, bash, and csh. It has also been tested on a Raspberry Pi on zsh and bash via SSH on iTerm.
* This command can only be run in a terminal. It is not designed to work if stdout is not a terminal. This includes piping and outputting to a file. Please use the regular `ping` command for those.
* If you encounter a Unicode error when running the command, try writing `PYTHONIOENCODING=utf-8` before the pingchart command. If your terminal can't display unicode, you can't use this program.
