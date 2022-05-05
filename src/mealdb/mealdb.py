# Copyright 2022 XXIV
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import http.client as client
from types import SimpleNamespace
import json
from urllib.parse import quote_plus


def http(endpoint):
    try:
        conn = client.HTTPSConnection('www.themealdb.com')
        conn.request('GET', f'/api/json/v1/1/{endpoint}')
        data = conn.getresponse().read().decode('UTF-8')
        conn.close()
        return data
    except:
        return None


def search(s: str):
    """
    Search meal by name
    :param s: meal name
    :return: list of objects
    """
    try:
        response = http(f"search.php?s={quote_plus(s)}")
        if response is not None and len(response) != 0:
            data = json.loads(response, object_hook=lambda d: SimpleNamespace(**d))
            if data.meals is not None:
                return data.meals
            else:
                return None
        else:
            return None
    except:
        return None


def search_by_letter(c: str):
    """
    Search meals by first letter
    :param c: meal letter
    :return: list of objects
    """
    try:
        response = http(f"search.php?f={c}")
        if response is not None and len(response) != 0:
            data = json.loads(response, object_hook=lambda d: SimpleNamespace(**d))
            if data.meals is not None:
                return data.meals
            else:
                return None
        else:
            return None
    except:
        return None


def search_by_id(i: int):
    """
    Search meal details by id
    :param i: meal id
    :return: object
    """
    try:
        response = http(f"lookup.php?i={i}")
        if response is not None and len(response) != 0:
            data = json.loads(response, object_hook=lambda d: SimpleNamespace(**d))
            if data.meals is not None:
                return data.meals[0]
            else:
                return None
        else:
            return None
    except:
        return None


def random():
    """
    Search a random meal
    :return: object
    """
    try:
        response = http("random.php")
        if response is not None and len(response) != 0:
            data = json.loads(response, object_hook=lambda d: SimpleNamespace(**d))
            if data.meals is not None:
                return data.meals[0]
            else:
                return None
        else:
            return None
    except:
        return None


def meal_categories():
    """
    Search meal by name
    :return: list of objects
    """
    try:
        response = http("categories.php")
        if response is not None and len(response) != 0:
            data = json.loads(response, object_hook=lambda d: SimpleNamespace(**d))
            if data.categories is not None:
                return data.categories
            else:
                return None
        else:
            return None
    except:
        return None


def filter_by_ingredient(s: str):
    """
    Filter by ingredient
    :param s: ingredient name
    :return: list of objects
    """
    try:
        response = http(f"filter.php?i={quote_plus(s)}")
        if response is not None and len(response) != 0:
            data = json.loads(response, object_hook=lambda d: SimpleNamespace(**d))
            if data.meals is not None:
                return data.meals
            else:
                return None
        else:
            return None
    except:
        return None


def filter_by_area(s: str):
    """
    Filter by area
    :return: list of objects
    """
    try:
        response = http(f"filter.php?a={quote_plus(s)}")
        if response is not None and len(response) != 0:
            data = json.loads(response, object_hook=lambda d: SimpleNamespace(**d))
            if data.meals is not None:
                return data.meals
            else:
                return None
        else:
            return None
    except:
        return None


def filter_by_category(s: str):
    """
    Filter by Category
    :param s: Category
    :return: list of objects
    """
    try:
        response = http(f"filter.php?c={quote_plus(s)}")
        if response is not None and len(response) != 0:
            data = json.loads(response, object_hook=lambda d: SimpleNamespace(**d))
            if data.meals is not None:
                return data.meals
            else:
                return None
        else:
            return None
    except:
        return None


def categories_filter():
    """
    List the categories filter
    :return: list of categories
    """
    try:
        response = http("list.php?c=list")
        if response is not None and len(response) != 0:
            data = json.loads(response, object_hook=lambda d: SimpleNamespace(**d))
            if data.meals is not None:
                data_list = []
                for i in data.meals:
                    data_list.append(i.strCategory)
                return data_list
            else:
                return None
        else:
            return None
    except:
        return None


def ingredients_filter():
    """
    List the ingredients filter
    :return: list the ingredients
    """
    try:
        response = http("list.php?i=list")
        if response is not None and len(response) != 0:
            data = json.loads(response, object_hook=lambda d: SimpleNamespace(**d))
            if data.meals is not None:
                return data.meals
            else:
                return None
        else:
            return None
    except:
        return None


def area_filter():
    """
    List the area filter
    :return: list the area
    """
    try:
        response = http("list.php?a=list")
        if response is not None and len(response) != 0:
            data = json.loads(response, object_hook=lambda d: SimpleNamespace(**d))
            if data.meals is not None:
                data_list = []
                for i in data.meals:
                    data_list.append(i.strArea)
                return data_list
            else:
                return None
        else:
            return None
    except:
        return None
