FROM python:3.10.10-bullseye

ENV APP_HOME=/code
WORKDIR $APP_HOME

RUN apt-get update && apt-get install -y openssh-client && \
    mkdir -p /home/appuser/.ssh && \
    touch /home/appuser/.ssh/known_hosts && \
    chmod 700 /home/appuser/.ssh && \
    chmod 644 /home/appuser/.ssh/known_hosts && \
    ssh-keyscan github.com >> /home/appuser/.ssh/known_hosts && \
    ssh-keyscan gitlab.com >> /home/appuser/.ssh/known_hosts

COPY ./requirements.txt $APP_HOME/requirements.txt

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r $APP_HOME/requirements.txt

RUN useradd appuser && chown -R appuser $APP_HOME
RUN touch /home/appuser/.gitconfig && chmod 666 /home/appuser/.gitconfig

RUN echo "[user]" >> /home/appuser/.gitconfig && \
    echo "    email = ivespauiniam@gmail.com" >> /home/appuser/.gitconfig && \
    echo "    name = Ives Costa" >> /home/appuser/.gitconfig && \
    chmod 666 /home/appuser/.gitconfig

RUN chmod -R u+rwX $APP_HOME 
USER appuser

RUN mkdir $APP_HOME/repositories
RUN mkdir $APP_HOME/keys

RUN chmod +w $APP_HOME

COPY . .

# Define o proprietário das pastas repositories e keys para o usuário appuser
USER root
RUN chown -R appuser:appuser /home/appuser/.ssh
RUN chown -R appuser:appuser $APP_HOME/repositories
USER appuser

EXPOSE 8000

CMD ["python", "-m", "debugpy", "--wait-for-client", "--listen","0.0.0.0:5678", "-m", "uvicorn", "main:api", "--host", "0.0.0.0", "--port", "8000", "--reload"]
