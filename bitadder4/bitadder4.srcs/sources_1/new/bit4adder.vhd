
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity bit4adder is
    Port ( C0, A1, A2, A3, A4, B1, B2, B3, B4: in STD_LOGIC;
           Cout, S1, S2, S3, S4: out STD_LOGIC
      );
end bit4adder;

architecture Behavioral of bit4adder is

    component fulladder 
         Port ( Cin, opA, opB: in STD_LOGIC;
                Cout, S: out STD_LOGIC
      );
    end component;

    Signal C1, C2, C3: STD_LOGIC;
    
begin

    U1: fulladder Port Map 
    (Cin => C0, opA => A1, opB => B1,
     Cout => C1, S => S1);
         
    U2: fulladder Port Map 
    (Cin => C1, opA => A2, opB => B2,
     Cout => C2, S => S2);

    U3: fulladder Port Map 
    (Cin => C2, opA => A3, opB => B3,
     Cout => C3, S => S3);
     
    U4: fulladder Port Map 
    (Cin => C3, opA => A4, opB => B4,
     Cout => Cout, S => S4);

end Behavioral;
