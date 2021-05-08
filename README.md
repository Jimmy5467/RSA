<h1 align="center">RSA </h1>
<div align="center">
  
<a href="https://github.com/Jimmy5467/RSA/stargazers"><img src="https://img.shields.io/github/stars/Jimmy5467/RSA?style=flat-square"/></a> 
<a href="https://github.com/Jimmy5467/RSA/network/members"><img src="https://img.shields.io/github/forks/Jimmy5467/RSA?style=flat-square"/></a> 
<a href="https://github.com/Jimmy5467/RSA/pullss"><img src="https://img.shields.io/github/issues-pr/Jimmy5467/RSA?&style=flat-square"/></a> 
<a href="https://github.com/Jimmy5467/RSA/issues"><img src="https://img.shields.io/github/issues/Jimmy5467/RSA?style=flat-square"/></a> 
<a href="https://github.com/Jimmy5467/RSA/graphs/contributors"><img src="https://img.shields.io/github/contributors/Jimmy5467/RSA?&style=flat-square&color=orange"/></a> 
<a href="https://github.com/Jimmy5467/RSA/blob/master/LICENSE"><img src="https://img.shields.io/github/license/Jimmy5467/RSA?&style=flat-square&color=1abc9c"/></a> 
<br>
  
![](https://img.shields.io/badge/Star-If_Liked-%23FF0000.svg?&style=flat-square&logoColor=white&color=white)
![](https://img.shields.io/badge/Fork-If_you_found_interesting-%23FF0000.svg?&style=flat-square&logoColor=white&color=white)<br>
</div>  

This project shows basic implementation of RSA algorithm from scratch. 

## RSA Mathematics
1. Select 2 large prime numbers, lets say p and q.
2. Multiply both large prime numbers, N = p * q.
3. Multiply again but by subtracting 1 from both, phiN = (p-1)*(q-1)
4. Select integer **e** such that : gcd(phiN, e) = 1 and  1 < e < phiN.
5. Now calculate **d** :  d = e^-1 (mod(phiN))

Public Key will be : PU = {e,N}

Private Key will be : PR = {d,N}

**Encryption**
Plain text(M) : M < n
Ciper test(C) : C = M^e mod n


**Encryption**
Ciper test(C) : C 
Plain text(M) : M = C^d mod n

## Implementation

Implementation is done in python and django. if you want to see only python implementaion and dont want user interface then you can directly go to [python](https://github.com/Jimmy5467/RSA/blob/master/Py_files_RSA/main.py)

And if want to run complete project then fork and download the repo and then use any python IDE of your choice, open this project and then download Django, run this code in Django. If you dont know how to run in django you can refer any youtube video. If you find something new then feel free to contribute.    
<!--


## Demo:

![](https://github.com/Jimmy5467/home_automation_using_camera/blob/master/gif.gif)
-->
## Facing any issues?

Feel free to [open an issue](https://github.com/Jimmy5467/RSA/issues/new?assignees=&labels=Query&title=Query). We are glad to help you. And is you have solution for that issue I will allocate to you. ❤️ 

If you have any more idea related to this project then please share your idea on jimmyaghera123@gmail.com. If time permits I will surely do some work on your project.


