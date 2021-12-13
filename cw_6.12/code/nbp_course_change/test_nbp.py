import pytest

import nbp_change as nbp


def mocklist(currency_code, days):
    return [4.6834, 4.6494, 4.6002, 4.5934, 4.5889, 4.5991, 4.5941, 4.6226, 4.6129, 4.6204], 'euro'


def test_calc_statistics(monkeypatch):

    # Podmieniamy w pliku zaimportowanym jako nbp funkcję get_courses na funkcję mocklist
    # Funkcja mocklist zwraca stałą tabelę z danymi skopiowanymi z outputu funkcji "get_courses" dla 10 dni
    monkeypatch.setattr(nbp, "get_courses", mocklist)

    result = nbp.calc_statistics(['EUR'], 10)
    assert result == {'EUR': {'change': 0.9865482341888372, 'course': 4.6204, 'full_name': 'euro'}}
