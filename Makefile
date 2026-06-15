.PHONY: generate run test build tidy secrets-encrypt secrets-decrypt

ENV ?= dev

generate:
	buf generate
	sqlc generate

run:
	ENV=$(ENV) go run ./cmd/server

build:
	go build -o bin/server ./cmd/server

test:
	go test ./...

tidy:
	go mod tidy

secrets-encrypt:
	sops --encrypt --output .env.$(ENV).enc .env.$(ENV)

secrets-decrypt:
	sops --decrypt --output .env.$(ENV) .env.$(ENV).enc
