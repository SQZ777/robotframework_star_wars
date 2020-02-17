** Settings **
Library    RequestsLibrary
Library    Collections
Library    custom_library.py
# Suite Setup    Create Session    swapi    https://e16bcb3f-db7a-4e1b-942a-6a88105e81b1.mock.pstmn.io
Suite Setup    Create Session    swapi    https://swapi.co/api

** Keywords **
Get All Vehicles From Page
    ${vehicle_list_from_page}=    Create List
    :FOR    ${page_number}    IN RANGE    1    100
    \    ${resp}=    Get Request    swapi    /vehicles/?page=${page_number}
    \    Should Be Equal As Strings    ${resp.status_code}    200
    \    ${vehicle_list_from_page}=    Combine Lists    ${vehicle_list_from_page}    ${resp.json()["results"]}
    \    Exit For Loop If    '${resp.json().get("next")}' == '${None}'
    [Return]    ${vehicle_list_from_page}

** Test Cases **
Count Species Of Films Six
    ${resp}=    Get Request    swapi    /films/6
    Should Be Equal As Strings    ${resp.status_code}    200
    ${species_len}=    Get Length    ${resp.json()["species"]}
    Log    ${species_len}

List all the film names and sort the name by episode_id
    ${resp}=    Get Request    swapi    /films/
    Should Be Equal As Strings    ${resp.status_code}    200
    ${sort_result}=    Sort List By Epsode Id    ${resp.json()["results"]}
    Log    ${sort_result}

Find out all vehicles which max_atmosphering_speed over 1000
    ${all_vehicles}=    Get All Vehicles From Page
    ${result}=    Find Max Atmosphering Speed Over    1000    ${all_vehicles}  # 此 Keyword 將會排除 速度為 unknown 的機器
    Log    ${result}
