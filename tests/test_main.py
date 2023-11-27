"""
File: main.py
Author: Steven (Kabbe)
Description: Entry point for the Stellaris Explorer project

For more information, see: https://github.com/xKabbe/stellaris-explorer
"""
from main import main


def test_main(capsys):
    main()

    captured_console_log = capsys.readouterr()
    assert captured_console_log.out.strip() == 'Hello World'
