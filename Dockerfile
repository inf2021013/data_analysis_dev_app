FROM python:3.11.8-slim-bullseye
WORKDIR /app
COPY . .
EXPOSE 8501
RUN bash script.sh
CMD [ "bash","-c","streamlit run ./app.py"]