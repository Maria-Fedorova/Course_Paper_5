from src.talk_to_user import user_interaction
from src.utils import load_data_database


def main():
    """
    Основная функция по работе с программой.
    """
    print(f"Пожалуйста, подождите, мы собираем для Вас информацию... Это может занять несколько минут")
    load_data_database()
    user_interaction()


if __name__ == "__main__":
    main()
