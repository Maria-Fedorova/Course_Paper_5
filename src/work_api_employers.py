from abc import ABC, abstractmethod

import requests

from settings import HH_URL_EMPLOYERS
from exceptions import ApiError


class ApiEmployer(ABC):
    """
    Абстрактный класс для получения информации о компаниях через API.
    """

    @abstractmethod
    def get_data_employers(self, company_ids: list[str]) -> list[dict]:
        """
        Абстрактный метод для получения информации о компаниях через API.
        :param company_ids: Список ids компаний.
        :return: Список со словарями с информацией о компаниях.
        """
        raise NotImplementedError


class HHApiEmployer(ApiEmployer):
    """
    Класс для получения информации о компаниях через API.
    """

    def get_data_employers(self, company_ids: list[str]) -> list[dict]:
        """
        Метод для получения информации о компаниях.
        :param company_ids: Список ids компаний.
        :return: Список со словарями с информацией о компаниях.
        """
        data_employers = []
        try:
            for company_id in company_ids:
                response_api_hh = requests.get(url=f"{HH_URL_EMPLOYERS}{company_id}").json()
                data_employers.append(response_api_hh)
            data_info_employers = [
                {"employer_id": int(data_employer["id"]), "employer_name": data_employer["name"].lower(),
                 "open_vacancies": data_employer["open_vacancies"], "url": data_employer["alternate_url"]} for
                data_employer in data_employers]
        except KeyError:
            raise ApiError()
        else:
            return data_info_employers
