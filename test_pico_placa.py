from pico_placa import main
import subprocess




def test_run_main():
    result = eval(subprocess.run(["python3", "pico_placa.py", "PBR-4551", "2021-10-20", "11:30"], capture_output=True, encoding='UTF-8').stdout)
    assert result == True