# DryOS
Some info about DryOS shell exposed via UART
 - This is likely the RTOS for wireless printing, not main firmware
 - It has same access to peripherals as ARM does


## Boot log
```
DRYOS version 2.3, release #0056
Copyright (C) 1997-2014 by CANON Inc.
version: v0.1.11
build: Nov 16 2017, 09:49:55
wlan available   
Dry> 
```

## DryOS commands
```
Dry> help
[Debug]
 task  sem  event  mq  mutex  cond  timer  itsk  isem  iflg  imbx  idtq  impf 
 impl  icyc  mkobjsize  kill  suspend  resume  release  delete  prio  mkcfg 
 objinfo  meminfo  xd  xm  cmp  pxthr  pxmq  stdlibcfg 
[Test]
 time  count  mktest  iotest  chkspi  chkit4 
[Miscellaneous]
 date  vers  exit  shutdown  dminfo 
[OTG]
 otg  otg_init  otg_cleanup 
[Network]
 netvers  eci  arp  dhcpc  slaup  ifconfig  mbufs  netstat  route  ping 
 rdinfo  tcputil  dnsutil  mib2  ipf  ipsec  ike 
[TMN]
 tm  rt  wp2pc 
[WELL]
 nell-attach  nell-detach  nell-wakeup  nlog  up  down  stat  scan  join 
 leave  wset  wget  wep  w12get  w12set  elog  uap  wfd 
[DUTAgent]
 duta 
[NT-Test]
 wprd  wtst  nsclog  phy_ctrl 
[GETIP6]
 getip6 
[ALINK]
 alinkcmd 
[AOSS]
 aoss 
[RACT]
 ract 
[WPSE]
 wpse  wpscmd  wpsc 
[WCF]
 wcf  wcfcmd 
[DHCPS]
 dhcps 
[NSPF]
 nspf 
[XHCOM]
 xhtest  xhlog 

```

## Version
```
Dry> vers
DRYOS version 2.3, release #0056
  Dry-MK 2.64
  Dry-DM 1.21
  Dry-FSM 0.10
  Dry-stdlib 1.55
  Dry-PX 1.13
  Dry-drylib 1.22
  Dry-shell 1.19
  Dry-command alpha 063

```
