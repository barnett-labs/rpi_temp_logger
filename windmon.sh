#! /bin/sh

a=10

while [ $a -ge 10 ]
do
   python anon2.py 
   a=`expr $a + 1`
done
