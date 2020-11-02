# MassiveScan
The program scans mass addresses for open port(s).
Enter in the file ips.txt addresses in CIDR format (ip/mask) and run MassiveScan.py.

Total:
Text files, whose name corresponds to the port, you want to scan. Inside valid ips.
<hr>

Tests (for 1 port):

9270 ips:

Nmap - 92,72 sec.

MassiveScan - 13,93 sec.

64700 ips:

Nmap - 1066,39 sec.

MassiveScan - 98,12 sec.

<hr>
