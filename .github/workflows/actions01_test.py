# -*- coding:utf-8 -*-
import pytest

def test_calc_addition():
  # Fonction qui teste le résultat de l'opération 2+4
    output = 2 + 4
    assert output == 6

def test_calc_substraction():
  # Fonction qui teste le résultat de 2-4
    output = 2 - 4
    assert output == -2

def test_calc_multiply():
  # Fonction qui teste le résultat de 2*4
    output = 2 * 4
    assert output == 8

def test_coucou():
  # Fonction qui teste si le résultat renvoie 'hello'
    output = 'hello'
    assert output == 'hello'
