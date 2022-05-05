# MealDB

[![](https://img.shields.io/github/v/tag/thechampagne/mealdb-py?label=version)](https://github.com/thechampagne/mealdb-py/releases/latest) [![](https://img.shields.io/github/license/thechampagne/mealdb-py)](https://github.com/thechampagne/mealdb-py/blob/main/LICENSE)

TheMealDB API client for **Python**.

### Download
[PyPI](https://pypi.org/project/mealdb/)

```
pip install mealdb
```

### Example

```py
from mealdb import search

for meal in search("Shawarma"):
    print(meal.strMeal)
```

### License

MealDB is released under the [Apache License 2.0](https://github.com/thechampagne/mealdb-py/blob/main/LICENSE).

```
 Copyright 2022 XXIV

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
```