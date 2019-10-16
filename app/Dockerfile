FROM python:3
ADD app.py /
ADD templates /templates
RUN pip install flask
RUN pip install redis
CMD [ "python", "./app.py" ]
EXPOSE 5000
