# -*- coding:utf-8 -*-
from Edgehub_testing_module import fuzzer_method, selenium_method, crolling, Device_module

if __name__ == "__main__":
    # Device interval, Time out
    Device_module.ModbusTCP_test(1000, 100)
    Device_module.ModbusRTU_test()
    Device_module.Fenet_test()
    Device_module.Cnet_test()
    Device_module.MELSEC_SERIAL_test()
    Device_module.MELSEC_ETH_test()
    