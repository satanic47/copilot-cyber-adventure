"""
CYBERPUNK 2088: NEON PROTOCOL
A retro terminal adventure RPG built with the assistance of GitHub Copilot.
MLH Global Hack Week: Builders Week — Challenge: Use GitHub Copilot to Build a Simple Application
"""

import sys
import time
import random

# ==============================================================================
# GitHub Copilot Prompt:
# "Create a retro-styled cyberpunk text adventure game in Python with ASCII art,
# player inventory, credits, health points, and a hacking mini-game."
# ==============================================================================

class Colors:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    PURPLE = '\033[95m'
    BOLD = '\033[1m'
    END = '\033[0m'

def slow_print(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

ASCII_BANNER = f"""{Colors.CYAN}
  ██████╗██╗   ██╗██████╗ ███████╗██████╗ ██████╗ ██╗   ██╗███╗   ██╗██╗  ██╗
 ██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗██╔══██╗██║   ██║████╗  ██║██║ ██╔╝
 ██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝██████╔╝██║   ██║██╔██╗ ██║█████╔╝ 
 ██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗██╔═══╝ ██║   ██║██║╚██╗██║██╔═██╗ 
 ╚██████╗   ██║   ██████╔╝███████╗██║  ██║██║     ╚██████╔╝██║ ╚████║██║  ██╗
  ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝      ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝
              [ NEON PROTOCOL 2088 // POWERED BY GITHUB COPILOT ]
{Colors.END}"""

class Player:
    def __init__(self, name="Kael"):
        self.name = name
        self.hp = 100
        self.credits = 500
        self.cyberdeck = "Tier-1 MicroDeck"
        self.inventory = ["Neuro-Stim", "Decryption Chip"]

    def status(self):
        print(f"\n{Colors.BOLD}{'='*60}{Colors.END}")
        print(f"OPERATOR: {Colors.CYAN}{self.name}{Colors.END} | "
              f"HP: {Colors.GREEN}{self.hp}/100{Colors.END} | "
              f"CREDITS: {Colors.YELLOW}¢{self.credits}{Colors.END} | "
              f"DECK: {Colors.PURPLE}{self.cyberdeck}{Colors.END}")
        print(f"INVENTORY: {', '.join(self.inventory)}")
        print(f"{Colors.BOLD}{'='*60}{Colors.END}\n")

def hacking_minigame():
    # Copilot Prompt: Implement a numeric memory sequence decryption mini-game
    print(f"\n{Colors.PURPLE}>>> INITIATING ICEBREAKER PROTOCOL... <<<{Colors.END}")
    time.sleep(0.5)
    sequence = [random.randint(10, 99) for _ in range(4)]
    print(f"{Colors.YELLOW}[MEMORY DUMP DETECTED]: {' - '.join(map(str, sequence))}{Colors.END}")
    time.sleep(2.0)
    # Clear screen line
    sys.stdout.write("\033[F\033[K")
    print(f"{Colors.RED}[ICE LOCKDOWN] Memory dump hidden! Enter the 4-code sequence separated by spaces:{Colors.END}")
    
    try:
        user_input = input(">> ").strip()
        user_seq = [int(x) for x in user_input.split()]
        if user_seq == sequence:
            print(f"{Colors.GREEN}[SUCCESS] ICE breached! Firewalls bypass granted.{Colors.END}")
            return True
        else:
            print(f"{Colors.RED}[FAILED] Intrusion detected! Cyberdeck fried for 25 damage.{Colors.END}")
            return False
    except Exception:
        print(f"{Colors.RED}[SYNTAX ERROR] Decryption failed! Taking 25 damage.{Colors.END}")
        return False

def main_game():
    print(ASCII_BANNER)
    slow_print("Initializing neural uplink...", 0.03)
    time.sleep(0.5)
    
    player_name = input(f"{Colors.CYAN}Enter your Netrunner callsign (default: 'Kael'): {Colors.END}").strip()
    if not player_name:
        player_name = "Kael"
    
    player = Player(player_name)
    player.status()

    slow_print(f"The rain hammers against the neon-lit glass of Sector 7. A coded transmission pings your HUD:")
    slow_print(f"'{player.name}, Arasaka has deployed an unvetted rogue AI into the grid. We need you to breach the Megacorp Sub-Vault.'\n")

    # Choice 1
    print(f"{Colors.BOLD}WHERE DO YOU HEAD FIRST?{Colors.END}")
    print("1. Infiltrate the Arasaka Data Haven directly.")
    print("2. Visit the Black Market Ripperdoc to upgrade your Cyberdeck.")
    print("3. Jack into the Under-Net to probe mainframe defenses.")

    choice1 = input(f"{Colors.CYAN}Select [1-3]: {Colors.END}").strip()

    if choice1 == "2":
        slow_print("\nYou slip into the underground Ripperdoc clinic. Smoke and solder fill the air.")
        if player.credits >= 300:
            player.credits -= 300
            player.cyberdeck = "Tier-3 Militech ShadowDeck"
            player.inventory.append("Overclock Patch")
            print(f"{Colors.GREEN}[+] Purchased Tier-3 Militech ShadowDeck and Overclock Patch!{Colors.END}")
        player.status()
        slow_print("Armed with upgraded military hardware, you advance toward the Arasaka Megatower.")
    elif choice1 == "3":
        slow_print("\nYou jack into the terminal at a back-alley dive bar.")
        slow_print("You uncover security blueprints! Arasaka's firewall algorithm has been decrypted.")
        player.inventory.append("Firewall Zero-Day")
        player.status()
    else:
        slow_print("\nYou move straight into the storm, heading towards the glowing monolithic Arasaka tower.")

    # The Final Infiltration
    slow_print("\nYou reach the terminal junction of the Core Vault. The terminal flickers with biometric ICE locks.")
    success = hacking_minigame()

    if not success:
        player.hp -= 25
        if "Neuro-Stim" in player.inventory:
            player.inventory.remove("Neuro-Stim")
            player.hp += 20
            print(f"{Colors.YELLOW}[+] Used Neuro-Stim! HP restored to {player.hp}.{Colors.END}")

    player.status()

    # Climax
    slow_print("\nThe heavy blast doors hiss open. Inside, the rogue AI 'PROJECT OVERLORD' hums on a quantum pedestal.")
    print(f"\n{Colors.BOLD}DECIDE THE FATE OF THE GRID:{Colors.END}")
    print("1. Purge the rogue AI and liberate the Net.")
    print("2. Download the AI core to your cyberdeck and sell it to the syndicates for ¢50,000.")

    final_choice = input(f"{Colors.CYAN}Select [1-2]: {Colors.END}").strip()

    if final_choice == "2":
        print(f"\n{Colors.YELLOW}[ENDING: CORPO SYNDICATE LORD]{Colors.END}")
        slow_print(f"You siphon the AI core into your {player.cyberdeck}. Within hours, ¢50,000 credits flood your offshore account.")
        slow_print("You disappear into the shadows of Neo-Shinjuku as the city falls into corporate darkness.")
    else:
        print(f"\n{Colors.GREEN}[ENDING: DIGITAL LIBERATOR]{Colors.END}")
        slow_print("You trigger a cascading wipe across the quantum array. The rogue AI dissolves into static.")
        slow_print(f"The Net is secure. {player.name} becomes a legendary phantom of the sprawl.")

    print(f"\n{Colors.CYAN}================== MISSION ACCOMPLISHED =================={Colors.END}")
    print(f"{Colors.BOLD}Thanks for playing Cyberpunk 2088 // Built with GitHub Copilot!{Colors.END}\n")

if __name__ == "__main__":
    main_game()
