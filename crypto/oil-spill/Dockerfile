FROM pwn.red/jail:0.4.0
COPY --from=sagemath/sagemath / /srv
COPY --chmod=755 server.sage /srv/app/run
COPY flag.txt /srv/app/
ENV JAIL_TIME=5400 JAIL_PIDS=20 JAIL_MEM=1G JAIL_CPU=1000 JAIL_TMP_SIZE=1M JAIL_ENV_HOME=/tmp
