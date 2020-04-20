# -*- coding:utf-8 -*-
from Edgehub_testing_module import fuzzer_method, selenium_method, crolling, Device_module

if __name__ == "__main__":
    Device_module.ModbusTCP_test(1000, 100, 20)