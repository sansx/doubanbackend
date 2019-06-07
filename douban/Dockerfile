FROM python:3
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pipenv
COPY . /spider/
WORKDIR /spider/
RUN pipenv install --deploy --ignore-pipfile
WORKDIR /spider/tutorial
CMD ["scrapy","crawl","dmoz"]
