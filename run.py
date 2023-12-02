"""
File: run.py
Author: Steven (Kabbe)
Description: Script to run the Stellaris Explorer Dash web application for exploring exoplanet data.

For more information, see: https://github.com/xKabbe/stellaris-explorer
"""
from app.frontend.dashboard import app

if __name__ == '__main__':
    app.run_server(debug=True)
