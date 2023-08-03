Solves: 3

Author: FizzBuzz101

Description:

A hardware quirk, a micro-architecture attack, and a kernel exploit all in one!

Note that the remote environment is on a Cascade Lake generation processor on a dedicated AWS instance.
KPTI is disabled in the distributed run script, as KPTI is automatically disabled on remote since the
kernel detects the relevant hardware mitigations KPTI was designed against. An AMD CPU will NOT work
for this challenge.

For those interested in building the kernel from scratch, feel free to download it from https://cdn.kernel.org/pub/linux/kernel/v6.x/linux-6.3.4.tar.xz

Flag: `corctf{tHIS is a SoFtWare ImPLEMENTAtioN isSuE. iNTeL PRoCESSORS ArE fuNCtIONinG AS PEr sPeCiFIcaTionS anD ThIS BEHavioR Is cORRecTly documEnteD IN tHE INTEL SofTwArE DEvELOPErs manual.}`