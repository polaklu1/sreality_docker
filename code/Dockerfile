FROM python:3.8
WORKDIR /code
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["./wrapper.sh"] 