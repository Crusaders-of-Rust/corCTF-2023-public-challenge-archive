FROM debian:latest as run
FROM pwn.red/jail:0.3.0
COPY --from=run / /srv
RUN mkdir /srv/app
RUN echo "corctf{sur3ly_th15_t1m3_17_w1ll_k1ll_c!!}" > /srv/app/flag.txt
COPY harem /srv/app/run
ENV JAIL_MEM=1G JAIL_CPU=500 JAIL_TIME=300 JAIL_POW=5000
