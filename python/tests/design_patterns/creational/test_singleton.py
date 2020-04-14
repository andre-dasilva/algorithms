import pytest

from design_patterns.creational.singleton import (SingletonClassic,
                                                  SingletonDecoratorClass,
                                                  SingletonDecoratorFunc)


@SingletonDecoratorClass
class TestDecoratedSingletonClass:
    pass


@SingletonDecoratorFunc
class TestDecoratedSingletonFunc:
    pass


def test_classic():
    first_instance = SingletonClassic.get_instance()
    second_instance = SingletonClassic.get_instance()

    assert first_instance == second_instance
    assert id(first_instance) == id(second_instance)


def test_classic_exception():
    with pytest.raises(TypeError):
        first_instance = SingletonClassic()


def test_decorator_class():
    first_instance = TestDecoratedSingletonClass.get_instance()
    second_instance = TestDecoratedSingletonClass.get_instance()

    assert first_instance == second_instance
    assert id(first_instance) == id(second_instance)


def test_decorator_class_exception():
    with pytest.raises(TypeError):
        first_instance = TestDecoratedSingletonClass()


def test_decorator_func():
    first_instance = TestDecoratedSingletonFunc()
    second_instance = TestDecoratedSingletonFunc()

    assert first_instance == second_instance
    assert id(first_instance) == id(second_instance)
