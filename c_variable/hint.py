from typing import List, Dict, Set, Tuple, Union, Final
data : Final[int] = 10 #Final 변경하지 말라는것
data = 20
print(data)

class A:
    pass

class B:
    @staticmethod
    def test(data :Union[int, str], number: int | float, data1: A, datas: List[int], data_dict: Dict[str, int]) -> int:
        # Union : [int + str] /number : int | float 두개 같음
        return 10

