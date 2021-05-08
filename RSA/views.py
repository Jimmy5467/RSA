from django.shortcuts import render
import requests
from subprocess import run, PIPE
import sys

sys.path.insert(1, './Py_files_RSA')

import key_generate,enc


def button(request):
    return render(request, 'home.html')


"""
def output(request):
    data = requests.get("https://google.com")
    print(data.text)
    data = data.text
    return render(request, 'home.html', {'data': data})
"""


def key_g(request):
    keysize = 32
    global p, q, e, d, N
    p, q, e, d, N = key_generate.generateKeys(keysize)
    """msg = "%s" % (sys.argv[1])"""
    return render(request, 'home.html', {'data1': e, 'data2': d})


def encryption(request):
    inp1 = request.POST.get('param1')
    en = enc.encrypt(e, N, inp1)
    return render(request, 'home.html', {'enc': en})


def decryption(request):
    inp2 = request.POST.get('param2')
    msg = ""

    parts = inp2.split()
    for part in parts:
        if part:
            c = int(part)
            msg += chr(pow(c, d, N))
    return render(request, 'home.html', {'dec': msg})


"""
def external(request):
    inp = request.POST.get('param')
    out = run([sys.executable, 'E://6th sem//CNS//miniproject//2//python//main.py', inp], shell=False, stdout=PIPE)
    print(out)
    return render(request, 'home.html', {'data1': out.stdout.decode('utf-8')})
"""
