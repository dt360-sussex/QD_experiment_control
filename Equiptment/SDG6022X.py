import pyvisa  # type: ignore
from pylablib.devices import AWG


class SDG6022X(AWG.GenericAWG):
    def __init__(self, addr):
        """
        Initialize the SDG6022X instrument.
        If addr is None, it takes the first available VISA resource.
        """
        # rm = pyvisa.ResourceManager()
        # self.instrument = rm.open_resource(addr)
        super().__init__(addr)
        
        # print(f"Connected to: {self.instrument.query('*IDN?')}")

    def control_off(self):
        """Turn output OFF"""
        self.instrument.write("C1:OUTP OFF")

    def control_on(self):
        """Turn output ON"""
        self.instrument.write("C1:OUTP ON")

    def set_freq(self, waveform="SQUARE", freq=100000, amp=1):
        """
        Set the waveform, frequency, and amplitude.
        Default: SQUARE wave, 100 kHz, 1 V amplitude
        """
        cmd = f"C1:BSWV WVTP,{waveform},FRQ,{freq},AMP,{amp}"
        self.instrument.write(cmd)
        
    def close(self):
        self.instrument.close()

if __name__ == "__main__":
    # Usage
    ip = "TCPIP::192.168.11.24::INSTR"    

    awg = SDG6022X(ip)  # or SDG6022X("TCPIP::192.168.0.10::INSTR") if you know the address

    # awg.control_on()
    # awg.set_freq()
    # awg.control_off()
    awg.close()
