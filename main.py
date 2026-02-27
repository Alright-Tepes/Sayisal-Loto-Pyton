import random
import time
import sys
import os

GREEN = "\033[32m"
BRIGHT_GREEN = "\033[92m"
RESET = "\033[0m"
BOLD = "\033[1m"
CLEAR = "\033[H\033[J"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def animate_number(target_number, position):
    """Belirli bir sayı için dönme animasyonu yapar."""
    for _ in range(15):
        random_temp = random.randint(1, 90)
        sys.stdout.write(f"\r{GREEN}Seçilen Sayılar: {RESET}")
        
        numbers_str = ""
        for i, val in enumerate(selected_numbers):
            numbers_str += f"{BRIGHT_GREEN}{val:02d}{RESET}  "
        
        sys.stdout.write(f"{numbers_str}{GREEN}{random_temp:02d}{RESET}")
        sys.stdout.flush()
        time.sleep(0.05)
    
    selected_numbers.append(target_number)
    
    sys.stdout.write(f"\r{GREEN}Seçilen Sayılar: {RESET}")
    numbers_str = ""
    for val in selected_numbers:
        numbers_str += f"{BRIGHT_GREEN}{val:02d}{RESET}  "
    sys.stdout.write(numbers_str)
    sys.stdout.flush()

def main():
    clear_screen()
    print(f"{BOLD}{BRIGHT_GREEN}")
    print("==========================================")
    print("      SAYISAL LOTO TAHMİN MAKİNESİ        ")
    print("==========================================")
    print(f"{RESET}")
    
    print(f"{GREEN}1 ile 90 arasından 6 şanslı sayı seçiliyor...{RESET}\n")
    
    global selected_numbers
    selected_numbers = []
    
    pool = list(range(1, 91))
    final_numbers = random.sample(pool, 6)
    final_numbers.sort()
    
    for i in range(6):
        animate_number(final_numbers[i], i)
        time.sleep(0.3)
    
    print(f"\n\n{BOLD}{BRIGHT_GREEN}Bol şanslar dileriz!{RESET}")
    print(f"{GREEN}=========================================={RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{GREEN}Program kapatıldı.{RESET}")
        sys.exit()
