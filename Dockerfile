FROM python:slim

WORKDIR /scripts

COPY constants.py .
COPY tg.py .
COPY idata.py .

ENTRYPOINT ["python", "idata.py"]
