FROM python:3.10-alpine

COPY base64url base64url

ENTRYPOINT [ "./base64url" ]
