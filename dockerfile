#base image
FROM python
COPY . /DockerAssignment
WORKDIR /DockerAssignment
CMD python Assignment1.py
