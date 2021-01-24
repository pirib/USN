
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;


entity fulladder is
    Port ( Cin, opA, opB: in STD_LOGIC;
           Cout, S: out STD_LOGIC
      );
end fulladder;

architecture Behavioral of fulladder is

begin
    S <= opA XOR opB xor Cin;
    Cout <= (opA AND opB) OR ((opA XOR opB) AND Cin);
end Behavioral;
