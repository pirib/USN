----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 08/23/2019 10:18:22 AM
-- Design Name: 
-- Module Name: alu_w1l - Behavioral
-- Project Name: 
-- Target Devices: 
-- Tool Versions: 
-- Description: 
-- 
-- Dependencies: 
-- 
-- Revision:
-- Revision 0.01 - File Created
-- Additional Comments:
-- 
----------------------------------------------------------------------------------


library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.numeric_std.ALL;

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx leaf cells in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity alu_w1l is
    Port ( 
        opA, opB: in std_logic_vector(3 downto 0);
        ctr: in std_logic_vector(2 downto 0);
        resC: out std_logic_vector(4 downto 0)
    );
end alu_w1l;

architecture arch of alu_w1l is
signal uopA, uopB, uresC: unsigned(4 downto 0);

begin
uopA <= unsigned('0' & opA);
uopB <= unsigned('0' & opB);

process(uopA, uopB, ctr)
begin



end process;

resC <= std_logic_vector(uresC);


end arch;
