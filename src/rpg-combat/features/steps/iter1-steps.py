from behave import *

from app.models.character import Character

@given(u'a character enters the world with the following attributes')
def step_impl(context):
    context.characters = []
    for row in context.table:
        context.characters.append(Character(name=row['name']))


@then(u'the new character has these initial attributes')
def step_impl(context):
    for row in context.table:
        for character in context.characters:
            assert str(character.level)==row['level']
            assert str(character.health)==row['health']
            assert str(character.alive).lower()==row['alive'].lower()

@when(u'the character receives damage')
def step_impl(context):
    for character in context.characters:
        for row in context.table:
            character.receive_damage(int(row['damage']))


@then(u'the character health is')
def step_impl(context):
    for row in context.table:
        for character in context.characters:
            assert str(character.health)==row['health']

@then(u'the character is Dead')
def step_impl(context):
    for character in context.characters:
        assert character.alive==False

@when(u'the character receives health')
def step_impl(context):
    for character in context.characters:
        for row in context.table:
            character.receive_health(int(row['health']))
