from robot.api import logger
import urllib3
urllib3.disable_warnings()


def sort_list_by_epsode_id(target_list):
    result = [None] * len(target_list)
    episode_ids = [None] * len(target_list)
    result = [None] * len(target_list)
    for i in range(len(target_list)):
        episode_ids[i] = target_list[i]["episode_id"]
    episode_ids.sort()

    result_index = 0
    for episode_id in episode_ids:
        for item in target_list:
            if item["episode_id"] == episode_id:
                result[result_index] = item["title"]
                result_index += 1
    return result


def find_max_atmosphering_speed_over(max_speed, vehicles):
    result = []
    for vehicle in vehicles:
        if vehicle["max_atmosphering_speed"] != "unknown":
            if int(vehicle["max_atmosphering_speed"]) > int(max_speed):
                result.append(vehicle["name"])
        # else:
        #   logger.console("unknonwSpeed:"+ vehicle["name"])
    return result
