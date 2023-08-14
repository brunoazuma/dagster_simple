# dagster_simple

This repository contains two sample dagster projects for simple pipeline orchestration. Both of them are a [Dagster](https://dagster.io/) project scaffolded with [`dagster project scaffold`](https://docs.dagster.io/getting-started/create-new-project).

## minimal

This project consists on the bare minimal architecture of a dagster instance for consuming APIs and storing it on a SQL database.

## blob_storage

This project consists on an evolution of the minimal architechture. It contains aditional layers for code repository and storage of raw data.

## Running

Just clone the repository, navigate on the desired project and run `docker-compose up` 😊