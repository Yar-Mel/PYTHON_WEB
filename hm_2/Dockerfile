
FROM python:3.11

WORKDIR /opt/personal_assistant/

RUN pip install pipenv && pipenv install

COPY Pipfile Pipfile.lock /opt/personal_assistant/
COPY personal_assistant/src /opt/personal_assistant/
COPY LICENSE /opt/personal_assistant/
COPY README.md /opt/personal_assistant/
COPY Dockerfile /opt/personal_assistant/

ENTRYPOINT ["python", "project_willy/__main__.py"]