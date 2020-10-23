FROM python:3.7
COPY File1.txt ./
COPY File2.txt ./
COPY File3.txt ./
ADD CCHW2.py /
CMD [ "python", "./CCHW2.py" ]