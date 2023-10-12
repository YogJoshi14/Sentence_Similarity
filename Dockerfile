FROM python:3.10-slim-buster

WORKDIR /app 

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . /app

# Expose port 8080 for Flask app
EXPOSE 8080

# Expose port 7860  for gradio app
EXPOSE 7860

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]