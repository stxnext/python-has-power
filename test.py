import argparse
import importlib
import inspect
import unittest

import php


class PHPAdvancedTestCase(unittest.TestCase):
    candidate_module = None

    @property
    def gas_car_class(self):
        return getattr(self.candidate_module, 'GasCar', None)

    @property
    def diesel_car_class(self):
        return getattr(self.candidate_module, 'DieselCar', None)

    @property
    def car_accident_class(self):
        return getattr(self.candidate_module, 'CarAccident')

    def test_gas_car_defined(self):
        """ GasCar defined in module """
        self.assertTrue(
            hasattr(self.candidate_module, 'GasCar'),
            msg='GasCar class not defined'
        )

    def test_diesel_car_defined(self):
        """ DieselCar defined in module """
        self.assertTrue(
            hasattr(self.candidate_module, 'DieselCar'),
            msg='DieselCar class not defined'
        )

    def test_gas_car_is_class(self):
        """ GasCar is a class type """
        self.assertTrue(
            inspect.isclass(self.gas_car_class),
            msg='GasCar is not a class'
        )

    def test_diesel_car_is_class(self):
        """ DieselCar is a class type """
        self.assertTrue(inspect.isclass(self.diesel_car_class))

    def test_gas_car_inheritance(self):
        """ GasCar should inherit from php.BaseCar"""
        self.assertTrue(
            issubclass(self.gas_car_class, php.BaseCar),
            msg='GasCar does not inherit from php.BaseCar'
        )

    def test_diesel_car_inheritance(self):
        """ DieselCar should inherit from php.BaseCar"""
        self.assertTrue(
            issubclass(self.diesel_car_class, php.BaseCar),
            msg='DieselCar does not inherit from php.BaseCar'
        )

    def test_gas_car_defines_drive(self):
        """ GasCar should define drive() method """
        self.assertTrue(
            hasattr(self.gas_car_class, 'drive'),
            msg='Method `drive` not defined in GasCar'
        )

    def test_diesel_car_defines_drive(self):
        """ DieselCar should define drive() method """
        self.assertTrue(
            hasattr(self.diesel_car_class, 'drive'),
            msg='Method `drive` not defined in DieselCar'
        )

    def test_gas_car_drive_is_function(self):
        """ GasCar.drive should be callable """
        self.assertTrue(
            inspect.isfunction(getattr(self.gas_car_class, 'drive')),
            msg='GasCar.drive is not callable'
        )

    def test_diesel_car_drive_is_function(self):
        """ DieselCar.drive should be callable """
        self.assertTrue(
            inspect.isfunction(getattr(self.diesel_car_class, 'drive')),
            msg='DieselCar.drive is not callable'
        )

    def test_gas_car_can_be_initialized(self):
        """ GasCar should be able to be initialized """
        try:
            instance = self.gas_car_class()
        except TypeError:
            self.fail('GasCar could not be initialized')
        else:
            self.assertTrue(instance)

    def test_diesel_car_can_be_initialized(self):
        """ DieselCar should be able to be initialized """
        try:
            instance = self.diesel_car_class()
        except TypeError:
            self.fail('DieselCar could not be initialized')
        else:
            self.assertTrue(instance)
        self.assertTrue(instance)

    def test_gas_car_instance_drive_is_bound(self):
        """ GasCar().drive should be bound to an instance """
        instance = self.gas_car_class()
        self.assertTrue(
            inspect.ismethod(instance.drive),
            msg='GasCar().drive is not a method'
        )

    def test_diesel_car_instance_drive_is_bound(self):
        """ DieselCar().drive should be bound to an instance """
        instance = self.diesel_car_class()
        self.assertTrue(
            inspect.ismethod(instance.drive),
            msg='DieselCar().drive is not a method'
        )

    def test_gas_car_drive_return_type(self):
        """ GasCar().drive should return a string """
        instance = self.gas_car_class()
        self.assertTrue(
            isinstance(instance.drive(), str),
            msg='GasCar().drive should return a `str`'
        )

    def test_diesel_car_drive_return_type(self):
        """ DieselCar().drive should return a string """
        instance = self.diesel_car_class()
        self.assertTrue(
            isinstance(instance.drive(), str),
            msg='DieselCar().drive should return a `str`'
        )

    def test_gas_car_drive_return_value(self):
        """ GasCar().drive should return 'brrrum' """
        instance = self.gas_car_class()
        self.assertEqual(
            instance.drive(),
            'brrrum',
            msg='GasCar().drive does not return \'brrrum\''
        )

    def test_diesel_car_drive_return_value(self):
        """ DieselCar().drive should return 'pyr pyr pyr' """
        instance = self.diesel_car_class()
        self.assertEqual(
            instance.drive(),
            'pyr pyr pyr',
            msg='GasCar().drive does not return \'pyr pyr pyr\''
        )

    def test_car_accident_defined(self):
        """ CarAccident class has been defined """
        self.assertTrue(
            hasattr(self.candidate_module, 'CarAccident'),
            msg='CarAccident class not defined'
        )

    def test_car_accident_is_class(self):
        """ CarAccident is a class type """
        self.assertTrue(
            inspect.isclass(self.car_accident_class),
            msg='CarAccident is not a class'
        )

    def test_car_accident_inheritance(self):
        """ CarAccident should inherit from php.BaseCar"""
        self.assertTrue(
            issubclass(self.car_accident_class, BaseException),
            msg='CarAccident does not inherit from BaseException'
        )

    def test_car_addition_raises_gas_gas(self):
        """ GasCar + GasCar should raise CarAccident """
        with self.assertRaises(
                self.car_accident_class,
                msg='GasCar + GasCar did not raise CarAccident'
        ) as exc:
            instance1 = self.gas_car_class()
            instance2 = self.gas_car_class()
            instance1 + instance2
            self.assertEqual(
                exc.msg, 'Crash!', msg='Exception message was not \'Crash!\''
            )

    def test_car_addition_raises_diesel_diesel(self):
        """ DieselCar + DieselCar should raise CarAccident """
        with self.assertRaises(
                self.car_accident_class,
                msg='DieselCar + DieselCar did not raise CarAccident'
        ) as exc:
            instance1 = self.diesel_car_class()
            instance2 = self.diesel_car_class()
            instance1 + instance2
            self.assertEqual(
                exc.msg, 'Crash!', msg='Exception message was not \'Crash!\''
            )

    def test_car_addition_raises_gas_diesel(self):
        """ GasCar + DieselCar should raise CarAccident """
        with self.assertRaises(
                self.car_accident_class,
                msg='GasCar + DieselCar did not raise CarAccident'
        ) as exc:
            instance1 = self.gas_car_class()
            instance2 = self.diesel_car_class()
            instance1 + instance2
            self.assertEqual(
                exc.msg, 'Crash!', msg='Exception message was not \'Crash!\''
            )

    def test_car_addition_raises_diesel_gas(self):
        """ DieselCar + GasCar should raise CarAccident """
        with self.assertRaises(
                self.car_accident_class,
                msg='DieselCar + GasCar did not raise CarAccident'
        ) as exc:
            instance1 = self.diesel_car_class()
            instance2 = self.gas_car_class()
            instance1 + instance2
            self.assertEqual(
                exc.msg, 'Crash!', msg='Exception message was not \'Crash!\''
            )

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("module", help="File with candidate answer")
    args = parser.parse_args()

    try:
        candidate_module = importlib.import_module(args.module)
    except:
        print('-' * 80)
        print('Could not import {}. Traceback information below'.format(
            args.module)
        )
        print('-' * 80)
        raise

    PHPAdvancedTestCase.candidate_module = candidate_module
    unittest.main(module='__main__', argv=[__file__])
