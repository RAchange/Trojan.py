Lab1 - Netcat 實驗環境建置
========================

## 第一步、安裝 php
- [macOS](https://tecadmin.net/install-php-macos/)
- [Ubuntu 18.04](https://phoenixnap.com/kb/install-php-7-on-ubuntu)
- [Windows](https://www.sitepoint.com/how-to-install-php-on-windows/)

## 第二步、下載專案
> git clone https://github.com/RAchange/Trojan.py

![](https://i.imgur.com/nBYVaU3.png)
## 第三步、架設網頁應用
> php -S 0.0.0.0:8888 -t ./trojan.py/Lab1

![](https://i.imgur.com/hTwD3xM.png)
## 第四步、測試
造訪 http://127.0.0.1:8888，測試是否架設成功?如果架設成功你應該看到這樣的頁面
![](https://i.imgur.com/SlVpkgO.png)