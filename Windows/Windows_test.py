# -*- coding:utf-8 -*-
from Edgehub_testing_module import fuzzer_method, selenium_method, crolling, Device_module

if __name__ == "__main__":
    # Device interval, Time out, count
    # Device_module.ModbusTCP_test(1000, 100, 1)
    # Device_module.ModbusTCP_test(1000, 100, 2)
    # Device_module.ModbusTCP_test(1000, 100, 4)
    # Device_module.ModbusTCP_test(1000, 100, 8)
    # Device_module.ModbusTCP_test(1000, 100, 16)
    # Device_module.ModbusTCP_test(1000, 100, 32)
    # Device_module.ModbusTCP_test(1000, 100, 64)
    # Device_module.ModbusTCP_test(1000, 100, 128)
    # Device_module.ModbusTCP_test(1000, 100, 256)
    # Device_module.ModbusTCP_test(1000, 100, 512)
    Device_module.ModbusTCP_test(1000, 100, 1024)
    # Device_module.ModbusTCP_test(1000, 100, 2048)
    # Device_module.ModbusTCP_test(1000, 100, 4096)
    # Device_module.ModbusTCP_test(1000, 100, 8192)


    # Device_module.ModbusRTU_test()
    # Device_module.Fenet_test()
    # Device_module.Cnet_test()
    # Device_module.MELSEC_SERIAL_test()
    # Device_module.MELSEC_ETH_test()
    