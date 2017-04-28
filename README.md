# PHP 2017 Advanced Test

Do rozwiązania zadania wymagany jest Python z gałęzi 3.x.

## Zadanie

W module `php` zdefiniowana została klasa `BaseCar`.

Twoim zadaniem jest napisać samodzielny plik pythonowy, który będzie  zawierać dwie klasy: `GasCar` i `DieselCar`.

Rozwiązanie musi spełniać następujące wymagania:


* Stwórz własny plik pythonowy (nazwa może być dowolna, jednak pamiętaj: *musi się go dać zaimportować*)
* Wewnątrz pliku stwórz dwie klasy: `GasCar` i `DieselCar`
  * Obie klasy muszą dziedziczyć z klasy `BaseCar` (musisz zaimportować moduł `php`)
  * Obie klasy muszą definiować metodę `drive()`
    * `drive()` dla `GasCar` musi zwracać string `'brrrum'`
    * `drive()` dla `DieselCar` musi zwracać string `'pyr pyr pyr'`
* Zdefiniuj własną klasę wyjątku nazwaną `CarAccident`
* Nadpisz metodę dodawania na obu klasach, tak, by próba dodania do siebie obiektów obu klas (np: `gas_car + diesel_car`) rzucała wyjątek `CarAccident`
  * Rzucony wyjątek musi posiadać wiadomość tekstową `'Crash!'`
  
## Testy

Możesz sprawdzić, czy Twój skrypt spełnia powyższe wymagania za pomocą naszego zestawu testów.

Przykładowo, jeśli Twój plik z rozwiązaniem nazywa się `example_solution.py`, możesz uruchomić testy przy pomocy następującego polecenia:

```bash
python3 test.py example_solution
```

Pamiętaj, by nie podawać rozszerzenia pliku (`.py`). Jeśli wszystko zostało wykonane prawidłowo, powinieneś zobaczyć wynik podobny do poniższego:

```bash
$ python3 test.py example_solution
..................
----------------------------------------------------------------------
Ran 25 tests in 0.001s
```

Jeśli nie, powinieneś zobaczyć listę nieudanych testów, razem z wszystkimi wyjątkami i komunikatami błędów, mówiących o tym dlaczego test się nie udał.
