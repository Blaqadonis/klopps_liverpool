FROM python:3.9-alpine

RUN pip install pandas scikit-learn waitress flask

WORKDIR /app

COPY ["predict.py", "model.bin", "./"]

EXPOSE 9696

ENTRYPOINT ["waitress", "--listen=*:9696", "predict:app"]