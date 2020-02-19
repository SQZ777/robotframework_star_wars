import unittest
import custom_library


class TestCustomLibrary(unittest.TestCase):

    def test_sort_list_by_epsode_id_input_hello_world_Should_Return_hello_world(self):
        test_data = [
            {"episode_id": 0,
             "title": "hello world!"}
        ]
        actual = custom_library.sort_list_by_epsode_id(test_data)
        self.assertEqual(["hello world!"], actual)

    def test_sort_list_by_epsode_id_input_1a_0b_Should_Return_0b1a(self):
        test_data = [
            {"episode_id": 1,
             "title": "a"},
            {"episode_id": 0,
             "title": "b"}
        ]
        actual = custom_library.sort_list_by_epsode_id(test_data)
        self.assertEqual(["b", "a"], actual)

    def test_sort_list_by_epsode_id_input_2a_1b_0c_Should_Return_0c1b2a(self):
        test_data = [
            {"episode_id": 2,
             "title": "a"},
            {"episode_id": 1,
             "title": "b"},
            {"episode_id": 0,
             "title": "c"}
        ]
        actual = custom_library.sort_list_by_epsode_id(test_data)
        self.assertEqual(["c", "b", "a"], actual)

    def test_find_max_atmosphering_speed_over_speed1000_10_car_Should_Return_empty_array(self):
        test_data = [
            {"max_atmosphering_speed": "10",
             "name": "Car"}
        ]
        actual = custom_library.find_max_atmosphering_speed_over(
            1000, test_data)
        self.assertEqual([], actual)

    def test_find_max_atmosphering_speed_over_speed1000_unknown_car_Should_Return_empty_array(self):
        test_data = [
            {"max_atmosphering_speed": "unknown",
             "name": "Car"}
        ]
        actual = custom_library.find_max_atmosphering_speed_over(
            1000, test_data)
        self.assertEqual([], actual)

    def test_find_max_atmosphering_speed_over_speed1000_1001_car_Should_Return_Car(self):
        test_data = [
            {"max_atmosphering_speed": "1001",
             "name": "Car"}
        ]
        actual = custom_library.find_max_atmosphering_speed_over(
            1000, test_data)
        self.assertEqual(["Car"], actual)

    def test_find_max_atmosphering_speed_over_speed1000_1000_car_1001_HaHaCar_Should_Return_HaHaCar(self):
        test_data = [
            {"max_atmosphering_speed": "1000",
             "name": "Car"},
            {"max_atmosphering_speed": "1001",
             "name": "HaHaCar"}
        ]
        actual = custom_library.find_max_atmosphering_speed_over(
            1000, test_data)
        self.assertEqual(["HaHaCar"], actual)

    def test_find_max_atmosphering_speed_over_speed1000_1990_car_1001_HaHaCar_Should_Return_Car_HaHaCar(self):
        test_data = [
            {"max_atmosphering_speed": "1990",
             "name": "Car"},
            {"max_atmosphering_speed": "1001",
             "name": "HaHaCar"}
        ]
        actual = custom_library.find_max_atmosphering_speed_over(
            1000, test_data)
        self.assertEqual(["Car", "HaHaCar"], actual)


if __name__ == '__main__':
    unittest.main()
