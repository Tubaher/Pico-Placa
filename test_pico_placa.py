from pico_placa import main
import subprocess
import pytest

# unit tests to be evaluated
@pytest.mark.parametrize("test_input, expected_output",
                        [
                            (["PBR4557", "2021_10_21", "07:30"], False),
                            (["PBR4557", "2021_10_21", "11:30"], True),
                            (["PBR4557", "2021_10_21", "16:30"], False),
                            (["PBR4557", "2021_10_21", "20:30"], True),
                            (["PBR4557", "2021_10_22", "19:20"], True),
                            (["PBR4557", "2021_10_23", "20:30"], True)
                        ]
                        )
def test_run_main(test_input, expected_output):
    """ This function will evaluated our pico_placa.py file with different arguments
    with an expected output """
    
    result = eval(subprocess.run(["python3", "pico_placa.py"] + test_input, capture_output=True, encoding='UTF-8').stdout)
    assert result == expected_output

