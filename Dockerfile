# for testing only.
# this is a simple python server that just listens on port 8080 and responds to any URL. prints the URL in the page
# so you can see what's going on. "useful"(?) for network testing or diagnostics

FROM python:slim-buster
COPY simpleserver.py /

EXPOSE 8080/tcp

ENTRYPOINT ["python3"]
CMD ["/simpleserver.py"]