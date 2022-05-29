# Quick start

You can find implementation in [app/models/character.py](./app/models/character.py)

## Problem to solve

[RPG Combat](RPG%20Combat.md)

## Without Docker

Prerequisites:

- Python >3.8

### Install and run

Prepare environment:

    pip -m venv .venv
    . .venv/Scripts/activate
    pip install -r requirements.txt

Run app:

    python app/app.py

Run test:

    behave
    behave -f html > bdd.html

## With Docker

    docker build -t rpg-kata .
    docker run --rm -it rpg-kata
