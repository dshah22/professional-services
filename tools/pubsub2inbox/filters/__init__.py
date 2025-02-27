#   Copyright 2021 Google LLC
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
from .regex import regex_replace
from .lists import split, index
from .strings import add_links, urlencode, generate_signed_url, json_encode, csv_encode, html_table_to_xlsx, make_list, read_gcs_object, filemagic
from .date import strftime, recurring_date
from .gcp import format_cost, get_cost


def get_jinja_filters():
    return {
        'regex_replace': regex_replace,
        'split': split,
        'index': index,
        'add_links': add_links,
        'urlencode': urlencode,
        'generate_signed_url': generate_signed_url,
        'strftime': strftime,
        'json_encode': json_encode,
        'csv_encode': csv_encode,
        'html_table_to_xlsx': html_table_to_xlsx,
        'format_cost': format_cost,
        'get_cost': get_cost,
        'recurring_date': recurring_date,
        'make_list': make_list,
        'read_gcs_object': read_gcs_object,
        'filemagic': filemagic
    }
