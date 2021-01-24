----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 09/09/2019 10:12:52 PM
-- Design Name: 
-- Module Name: top_level_edice - Behavioral
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

entity top_level_edice is
port (
     clk, rst, cheat, run: in std_logic; 
     cheat_in : in std_logic_vector(2 downto 0);
     ed_out : out std_logic_vector(2 downto 0);
     seg: out std_logic_vector(6 downto 0)
);
end top_level_edice;

architecture Behavioral of top_level_edice is

    signal ed_buffer: std_logic_vector(2 downto 0);

    component edice
        Port (clk, rst, cheat, run: in std_logic; 
              cheat_in : in std_logic_vector(2 downto 0);
              ed_out : out std_logic_vector(2 downto 0));
    end component;

    component to7seg
        Port (seg_in : in std_logic_vector(2 downto 0);
              seg: out std_logic_vector(6 downto 0));
    end component;


begin

U1: edice Port Map (
    clk => clk, rst => rst, cheat => cheat, run => run,
    cheat_in => cheat_in, ed_out => ed_buffer
);

U2: to7seg Port Map (
    seg_in => ed_buffer, seg => seg
);

ed_out <= ed_buffer;

end Behavioral;
