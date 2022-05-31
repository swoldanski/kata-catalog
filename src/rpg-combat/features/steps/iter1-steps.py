from behave import *
from hamcrest import assert_that, equal_to, equal_to_ignoring_case, is_, is_not

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
            assert_that(str(character.level), equal_to(row['level']))
            assert_that(str(character.health), equal_to(row['health']))
            assert_that(str(character.alive),
                        equal_to_ignoring_case(row['alive']))


@ when(u'the character receives damage')
def step_impl(context):
    for character in context.characters:
        for row in context.table:
            character.receive_damage(int(row['damage']))


@ then(u'the character health is')
def step_impl(context):
    for row in context.table:
        for character in context.characters:
            assert_that(str(character.health), equal_to(row['health']))


@ then(u'the character is Dead')
def step_impl(context):
    for character in context.characters:
        assert_that(character.alive, is_not(True))


@ when(u'the character receives health')
def step_impl(context):
    for character in context.characters:
        for row in context.table:
            character.receive_health(int(row['health']))
