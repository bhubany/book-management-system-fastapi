FROM python:3.10-alpine 

WORKDIR /app

COPY . .

RUN python -m venv env

RUN source env/bin/activate 

RUN pip install -r requirements.txt

RUN chmod +x ./entry_point.sh

ENTRYPOINT [ "./entry_point.sh" ]