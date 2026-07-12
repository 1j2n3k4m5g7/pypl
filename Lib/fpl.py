from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from builtins import print as napisz
    from builtins import input as wprowadz
    from builtins import len as dlugosc
    from builtins import range as zakres
    from builtins import type as typ
    from builtins import id as id_obiektu
    from builtins import dir as spis
    from builtins import str as tekst
    from builtins import int as liczba
    from builtins import float as ulamek
    from builtins import list as lista
    from builtins import dict as slownik
    from builtins import set as zbior
    from builtins import tuple as krotka
    from builtins import bool as logiczny

    from builtins import Exception as BladBledu
    from builtins import ValueError as BladWartosci
    from builtins import TypeError as BladTypu
    from builtins import NameError as BladNazwy
    from builtins import IndexError as BladIndeksu
    from builtins import KeyError as BladKlucza
    from builtins import ZeroDivisionError as BladDzieleniaPrzezZero
    from builtins import property as wlasnosc
    from builtins import classmethod as metoda_klasy
    from builtins import staticmethod as metoda_statyczna
else:
    napisz = print
    wprowadz = input
    dlugosc = len
    zakres = range
    typ = type
    id_obiektu = id
    spis = dir
    tekst = str
    liczba = int
    ulamek = float
    lista = list
    slownik = dict
    zbior = set
    krotka = tuple
    logiczny = bool
    BladBledu = Exception
    BladWartosci = ValueError
    BladTypu = TypeError
    BladNazwy = NameError
    BladIndeksu = IndexError
    BladKlucza = KeyError
    BladDzieleniaPrzezZero = ZeroDivisionError
    wlasnosc = property
    metoda_klasy = classmethod
    metoda_statyczna = staticmethod
