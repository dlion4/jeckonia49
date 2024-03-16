
#pull python versionm
FROM python:3.9
# copy code 
COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

RUN pip install --upgrade pip


EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "8000" ]


