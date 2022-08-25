# syntax=docker/dockerfile:1.4
FROM alpine as builder
RUN apk add raptor2
WORKDIR /ontology   
COPY . .
RUN ./scripts/combine

# "from scratch" causes "no command specified"
FROM busybox
COPY --link --from=builder /ontology/dist /ontology/dist
WORKDIR /ontology/dist
VOLUME /ontology/dist
