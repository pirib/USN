-- USN VHDL 101 course
-- 16-bit binary U/D counter

library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity counter is
        port (clk, reset, en, direction, clear, load: in std_logic;
              c_out: out std_logic_vector (7 downto 0)
              );
end counter;

architecture barch of counter is
signal c_int: unsigned(7 downto 0):= "10000000";

begin
    process (clk)
          begin
                if rising_edge(clk) then
                      if reset='1' then
                            c_int <= (others => '0');
                      else
                          if load='1' then
                                c_int <= "10000000";
                          elsif load='0' and en='1' then
                                if direction='1' then
                                    c_int <= c_int + 1;
                                else
                                    c_int <= c_int - 1;
                                end if;
                          end if;
                      end if;
                      
                      if clear='1' then
                            c_out <= (others => '0');
                      end if;
                end if;
            c_out <= std_logic_vector(c_int);
        end process;


end barch;





