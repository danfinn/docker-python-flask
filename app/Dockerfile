FROM python:3
ADD app.py /
ADD templates /templates
ADD static /static
RUN pip install flask
RUN pip install redis
CMD [ "python", "./app.py" ]
EXPOSE 5000
