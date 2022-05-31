from behave import *
from hamcrest import assert_that, equal_to, equal_to_ignoring_case, is_, is_not

from app.models.character import Character


@ when(u'the character receives damage from')
def step_impl(context):
    for character in context.characters:
        for row in context.table:
            name = row['name']
            enemy = Character(name)
            if character.name == name:
                enemy = character
            amount = int(row['damage'])
            character.receive_damage(damage=amount, attacker=enemy)


@ when(u'the character receives health from')
def step_impl(context):
    for character in context.characters:
        for row in context.table:
            name = row['name']
            friend = Character(name)
            if character.name == name:
                friend = character
            amount = int(row['health'])
            character.receive_health(health=amount, healer=friend)


@given(u'the character current level is {lvl}')
def step_impl(context, lvl):
    for character in context.characters:
        character.level = int(lvl)


@when(u'the character receives damage from others with some level')
def step_impl(context):
    for character in context.characters:
        for row in context.table:
            level = int(row['level'])
            enemy = Character(level)
            enemy.level = level
            amount = int(row['damage'])
            character.receive_damage(damage=amount, attacker=enemy)
