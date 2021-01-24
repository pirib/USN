library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity to7seg is 
port (seg_in : in std_logic_vector(2 downto 0);
      seg: out std_logic_vector(6 downto 0));
end to7seg;

architecture b2 of to7seg is
  
BEGIN

    seg <= 
    "1111001" when seg_in = "001" else      -- 1   
    "0100100" when seg_in = "010" else      -- 2     
    "0110000" when seg_in = "011" else      -- 3     
    "0011001" when seg_in = "100" else      -- 4     
    "0010010" when seg_in = "101" else      -- 5     
    "0000010" when seg_in = "110" ;         -- 6     
  
END b2;


