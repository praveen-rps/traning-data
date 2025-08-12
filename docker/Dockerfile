FROM python:alpine3.21
RUN mkdir /project
RUN pip install flask
ADD app.py /
EXPOSE 5000:5000
CMD ["python", "/app.py"]
