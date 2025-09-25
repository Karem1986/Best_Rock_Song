FROM python:slim-trixie

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# Following container security best practices by creating a dedicated system user with no shell access. This minimizes riskS.
RUN groupadd -r oldies && useradd --no-log-init -r -g oldies oldies
RUN chown -R oldies:oldies /app
USER oldies

EXPOSE 8080

CMD ["python", "oldies_songs.py"]
