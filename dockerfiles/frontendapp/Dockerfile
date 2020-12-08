FROM python:2.7.17
WORKDIR /usr/src/app
RUN pip install flask
RUN pip install requests
RUN pip install flask-mysqldb
ENV FLASK_APP frontend.py
ENV FLASK_RUN_HOST 0.0.0.0
ADD frontend.py  /usr/src/app/
CMD ["flask", "run"] 
