FROM python:slim

# Upgrade pip, install pipenv
RUN pip install --upgrade pip
RUN pip install pipenv

WORKDIR /app

# Copy files that list dependencies
COPY Pipfile.lock Pipfile ./

# Generate requirements.txt and install dependencies from there
RUN pipenv requirements > requirements.txt
RUN pip install -r requirements.txt
RUN playwright install
RUN playwright install-deps

COPY constants.py .
COPY tg.py .
COPY idata.py .

ENTRYPOINT ["python", "idata.py"]
