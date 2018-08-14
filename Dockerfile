FROM python:3
ADD . /code
WORKDIR /code
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r ./requirements.txt
EXPOSE 8050
CMD [ "python", "app.py" ]
