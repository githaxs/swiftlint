FROM norionomura/swiftlint:latest as swiftlint

FROM public.ecr.aws/lambda/python:3.8 as deps
COPY --from=swiftlint /usr/bin/swiftlint /usr/bin

ARG GITHUB_TOKEN

RUN yum install -y git libcurl4-openssl-dev libxml2-dev glibc-2.7

COPY requirements.txt .
RUN python3.8 -m pip install -r requirements.txt

COPY . .

# Command can be overwritten by providing a different command in the template directly.
CMD ["handler.lambda_handler"]
