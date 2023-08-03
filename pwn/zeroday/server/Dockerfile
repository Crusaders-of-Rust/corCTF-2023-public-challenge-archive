FROM alpine:latest as run
RUN apk add --no-cache qemu-system-x86_64

FROM pwn.red/jail:0.3.0
COPY --from=run / /srv
RUN mkdir /srv/app
COPY run bzImage initramfs.cpio.gz /srv/app/
ENV JAIL_MEM=5G JAIL_CPU=500 JAIL_TIME=300 JAIL_POW=20000

