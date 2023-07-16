# sort fun

```bash
aaron@Aarons-Air sort-fun % wc -l outputs.txt
 10000000 outputs.txt
aaron@Aarons-Air sort-fun % ls -lha outputs.txt
-rw-r--r--  1 aaron  staff   717M 17 Jul 09:15 outputs.txt

aaron@Aarons-Air sort-fun % time ./sorthead.sh > /dev/null
./sorthead.sh > /dev/null  15.06s user 0.98s system 96% cpu 16.566 total
aaron@Aarons-Air sort-fun % time python3 sorthead.py > /dev/null
python3 sorthead.py > /dev/null  4.02s user 0.38s system 497% cpu 0.885 total

```
