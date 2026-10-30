
import random

def play_game():
    secret_number = random.randint(1, 100)
    max_attempts = 5
    attempts = 0

    print("\n================================")
    print("       بازی حدس اعداد")
    print("================================")
    print("من یک عدد بین 1 تا 100 انتخاب کرده‌ام.")
    print("شما 5 فرصت برای حدس زدن دارید.\n")

    while attempts < max_attempts:

        try:
            guess = int(input("عدد مورد نظر خود را وارد کنید: "))

            if guess < 1 or guess > 100:
                print("خطا! عدد باید بین 1 تا 100 باشد.")
                continue

        except ValueError:
            print("خطا! لطفاً فقط عدد وارد کنید.")
            continue

        attempts += 1
        remaining = max_attempts - attempts

        print(f"\nتلاش {attempts} از {max_attempts}")
        print(f"جان باقی‌مانده: {remaining}")

        if guess == secret_number:
            print("\nتبریک! شما برنده شدید.")

            if attempts == 1:
                print("رتبه شما: نمونه‌ای!")
            elif attempts == 2:
                print("رتبه شما: بسیار خوبی!")
            elif attempts == 3:
                print("رتبه شما: خوب!")
            elif attempts == 4:
                print("رتبه شما: قبول!")
            elif attempts == 5:
                print("رتبه شما: با شانس بردی!")

            return

        difference = abs(guess - secret_number)

        if guess > secret_number:
            print("عدد مخفی کوچک‌تر است.")
        else:
            print("عدد مخفی بزرگ‌تر است.")

        if difference <= 5:
            print("خیلی نزدیکی!")
        elif difference <= 15:
            print("نزدیکی، ولی هنوز فاصله داری!")
        else:
            print("خیلی دوری!")

        print("--------------------------------")

    print("\nمتأسفانه فرصت‌های شما تمام شد!")
    print(f"عدد صحیح {secret_number} بود.")
    print("شما در این دور برنده نشدید.")



while True:
    play_game()

    answer = input("\nآیا می‌خواهید دوباره بازی کنید؟ (بله/خیر): ")

    if answer.strip().lower() not in ["بله", "بلی", "yes", "y"]:
        print("\nممنون از بازی شما. خداحافظ!")
        break
