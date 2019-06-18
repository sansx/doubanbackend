FROM python:3
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pipenv
COPY . /spider/
WORKDIR /spider/
RUN pipenv install --deploy --ignore-pipfile
WORKDIR /spider/tutorial
EXPOSE 8000
CMD ["pipenv", "run", "gunicorn", "-b", ":5000", "--access-logfile", "-", "--error-logfile", "-", "doubanAPI:app" ]
