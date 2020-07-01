FROM tiangolo/uwsgi-nginx-flask:latest
COPY ./ /app
RUN pip install -r /app/requirements.txt
CMD ["python3","/app/main.py"]