FROM python:3.8.7-slim-buster
RUN mkdir src && mkdir target_directory_mount && mkdir source_directory_mount
COPY ./src /src
WORKDIR /src
ENTRYPOINT python3 index.py "/source_directory_mount" "/target_directory_mount"
