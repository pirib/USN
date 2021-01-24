LIBRARY ieee;
USE ieee.std_logic_1164.ALL; 

ENTITY counter_tb IS 
END counter_tb;

ARCHITECTURE barch OF counter_tb IS

-- Component Declaration for the Unit Under Test (UUT)

COMPONENT counter
 port (clk, reset, en, direction, clear, load: in std_logic;
      c_out: out std_logic_vector(7 downto 0)
        );
END COMPONENT;

signal clk, reset, en, direction, clear, load: std_logic := '0'; -- module inputs
signal c_out: std_logic_vector(7 downto 0); -- module outputs


BEGIN
    -- Instantiate the Unit Under Test (UUT) 
    uut: counter PORT MAP (
       clk => clk, reset => reset, en => en, direction => direction, clear=>clear,
       load=>load, c_out => c_out
    );

clk <= not clk after 10ns;

process
    begin 
        en        <= '1';
        direction <= '1';    


    wait;
end process; 
END;