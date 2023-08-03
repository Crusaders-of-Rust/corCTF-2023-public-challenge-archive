FROM python:3.10-alpine

# install packages
RUN apk update
RUN apk add --no-cache gcc musl-dev python3-dev libffi-dev freetype-dev

# permissions and nonroot user stuff
RUN adduser -D nonroot
RUN mkdir /home/app/ && chown -R nonroot:nonroot /home/app
WORKDIR /home/app
USER nonroot

# copy all the files to the container
COPY --chown=nonroot:nonroot app/ .

# venv
ENV VIRTUAL_ENV=/home/app/venv

# python setup and installing deps
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["gunicorn", "-w", "3", "-t", "60", "-b", "0.0.0.0:8000", "wsgi:application"]
