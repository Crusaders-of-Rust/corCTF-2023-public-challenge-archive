FROM ubuntu:22.04

ENV DEBIAN_FRONTEND noninteractive

RUN useradd -m corchatv2 && \
    mkdir /opt/corchatv2 && \
    mkdir /opt/corchatv2/usr && \
    mkdir /opt/corchatv2/bin && \
    cp -R /lib* /opt/corchatv2 && \
    cp -R /usr/lib* /opt/corchatv2/usr && \
    cp /bin/* /opt/corchatv2/bin

RUN mkdir /opt/corchatv2/dev && \
    mknod /opt/corchatv2/dev/null c 1 3 && \
    mknod /opt/corchatv2/dev/zero c 1 5 && \
    mknod /opt/corchatv2/dev/random c 1 8 && \
    mknod /opt/corchatv2/dev/urandom c 1 9 && \
    chmod 666 /opt/corchatv2/dev/*

COPY ./server.bin /opt/corchatv2/server.bin
COPY ./flag.txt /opt/corchatv2/flag.txt

RUN chmod -R o-w /opt/corchatv2/ && \
    chmod +x /opt/corchatv2/server.bin

EXPOSE 5000
CMD ["/usr/sbin/chroot", "--userspec=1000:1000", "/opt/corchatv2", "./server.bin", "5000"]
