FROM debian:12-slim AS run
RUN apt-get update && apt-get -y install qemu-system-x86 && rm -rf /var/lib/apt/lists/*

FROM pwn.red/jail:0.3.0
COPY --from=run / /srv
RUN mkdir /srv/app
COPY run bzImage initramfs.cpio.gz /srv/app/
ENV JAIL_MEM=5G JAIL_CPU=500 JAIL_TIME=300 JAIL_POW=45000
