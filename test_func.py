import pytest
import services.csv_service

# python3 test_func.py "assets/compositions.csv" ,

@pytest.fixture(params = services.csv_service.CsvService.get_data_from_csv("assets/compositions.csv",','))
def need_data(request):  # The parameter request system encapsulation parameter is passed in
    return request.param  # Get the single data from the list of data.


class Test_FUNC:

    def test_data(self, need_data):
        print("------->test_data")
        b = ( "-" in str(need_data) or "·" in str(need_data) or "%" in str(need_data) or " " in str(need_data) or "(" in str(need_data))==0
        if b == 0:
            print(need_data)
        assert b

if __name__ == '__main__':
    pytest.main(['-s', 'test_func.py'])
    # pytest.main()