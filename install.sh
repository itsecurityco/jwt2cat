#!/usr/bin/env bash

mv ../jwt2cat /usr/share/
ln -s /usr/share/jwt2cat/jwt2cat.py /usr/bin/jwt2cat
chmod a+x /usr/bin/jwt2cat

echo "jwt2cat installed into /usr/bin/"
