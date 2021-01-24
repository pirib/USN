library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity edice_tb is
end edice_tb;

architecture Behavioral of edice_tb is

constant clk_period : time := 10 ns;

COMPONENT edice
port (
     clk, rst, cheat, run: in std_logic; 
     cheat_in : in std_logic_vector ( 2 downto 0 );
     ed_out : out std_logic_vector ( 2 downto 0 )
);
END COMPONENT;

signal clk, rst, cheat, run: std_logic;
signal cheat_in: std_logic_vector ( 2 downto 0);
signal ed_out: std_logic_vector ( 2 downto 0);

BEGIN
    -- Instantiate the Unit Under Test (UUT)
    uut: edice port map (
         clk => clk, rst => rst,
         cheat => cheat, run => run,
         cheat_in => cheat_in, ed_out => ed_out
    );

clk_process: process
   begin
      clk <= '0';
      wait for clk_period;
      clk <= '1';
      wait for clk_period;
   end process;


-- Stimulus process
stim: process
begin
    cheat <= '0';
    rst <= '0';
    run <= '1';
    wait for 400ns;

--    rst <= '1';
    run <= '0';
    wait for 200ns;

    rst <= '0';
    run<='1';
    cheat <= '1';
    cheat_in <= "000";
    wait for 200ns;
    
    wait;
    
end process;
END;
