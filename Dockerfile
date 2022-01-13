FROM python:3.8

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

COPY . /usr/src/app/
RUN pip install --no-cache -r requirements.txt

EXPOSE 8088

CMD ["python","startmotors.py"]
