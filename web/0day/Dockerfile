FROM node:18

WORKDIR /opt
COPY package* ./
RUN npm ci

COPY web.js ./
COPY flag.txt /flag.txt

CMD ["node", "web.js"]