FROM python:3.8-slim
RUN pip install pipenv
RUN pip install pandas scikit-learn==1.2.0 flask requests
RUN pip install waitress
WORKDIR /app

COPY ["predict.py", "model.bin", "./"]

ENTRYPOINT ["waitress-serve",  "--listen=0.0.0.0:9696", "predict:app"]