## *jwt2cat* ##

Convert a JWT to **hashcat** format.

### Usage ###
```sh
python3 jwt2cat.py JWT
```

### Example ###
```sh
python3 jwt2cat.py eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.XbPfbIHMI6arZ3Y922BhjWgQzWXcXNrz0ogtVhfEd2o > hash.txt
```

```sh
cat hash.txt 
5db3df6c81cc23a6ab67763ddb60618d6810cd65dc5cdaf3d2882d5617c4776a:eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ
```

```sh
hashcat -m 1450 -a 0 hash.txt 10-million-password-list-top-1000000.txt --force
hashcat (v5.1.0) starting...
...
Dictionary cache hit:
* Filename..: 10-million-password-list-top-1000000.txt
* Passwords.: 999999
* Bytes.....: 8529110
* Keyspace..: 999999

5db3df6c81cc23a6ab67763ddb60618d6810cd65dc5cdaf3d2882d5617c4776a:eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ:secret
                                                 
Session..........: hashcat
Status...........: Cracked
Hash.Type........: HMAC-SHA256 (key = $pass)
Hash.Target......: 5db3df6c81cc23a6ab67763ddb60618d6810cd65dc5cdaf3d28...MDIyfQ
Time.Started.....: Mon Apr 27 22:16:30 2020 (0 secs)
Time.Estimated...: Mon Apr 27 22:16:30 2020 (0 secs)
Guess.Base.......: File (10-million-password-list-top-1000000.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:    72912 H/s (1.66ms) @ Accel:1024 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests, 1/1 (100.00%) Salts
Progress.........: 4096/999999 (0.41%)
Rejected.........: 0/4096 (0.00%)
Restore.Point....: 0/999999 (0.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidates.#1....: 123456 -> 12345678q

Started: Mon Apr 27 22:16:29 2020
Stopped: Mon Apr 27 22:16:32 2020
```

