library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity edice is 
port (clk, rst, cheat, run: in std_logic; 
      cheat_in : in std_logic_vector(2 downto 0);
      ed_out : out std_logic_vector(2 downto 0));
end edice;

architecture b1 of edice is

-- initializing value is needed or it will be left as undefined!
signal ctr: unsigned(2 downto 0) := "001";
signal ffout: unsigned(2 downto 0) := (others => '0');

BEGIN

-- state register section
process (clk, rst)
   begin

    if (rst = '1') then ffout<= "001";      
    elsif rising_edge(clk) and run='1' then 
        ctr <= ctr + 1; ffout <= ctr;          
        if cheat='0' and ctr = "110"  then ctr <="001";
        elsif cheat='1' and (ctr = "111" or ctr = "000") then ffout <= unsigned(cheat_in);
        end if;
    end if;
       
end process;

-- output section
ed_out <= std_logic_vector(ffout);

END b1;




