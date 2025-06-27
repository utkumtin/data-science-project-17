import pytest
import pandas as pd
import numpy as np
import requests
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tasks.task_manager import *

def test_five_number_summary():
    result = five_number_summary([1, 2, 3, 4, 5, 6, 7])
    assert result['min'] == 1
    assert result['median'] == 4
    assert result['max'] == 7

def test_detect_outliers():
    assert detect_outliers([10, 12, 14, 100]) == [100]

def test_calculate_skewness():
    skew = calculate_skewness([1, 2, 3, 4, 100])
    assert round(skew, 2) > 0  # sağa çarpık

def test_is_skewed():
    assert is_skewed([1, 2, 3, 4, 100]) == 'right'

def test_calculate_covariance():
    cov = calculate_covariance([1, 2, 3], [4, 5, 6])
    assert round(cov, 2) == 1.0

def test_calculate_correlation():
    corr = calculate_correlation([1, 2, 3], [4, 5, 6])
    assert round(corr, 2) == 1.0

def send_post_request(url: str, data: dict, headers: dict = None):
    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()  # hata varsa exception fırlatır
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
    except Exception as err:
        print(f"Other error occurred: {err}")

class ResultCollector:
    def __init__(self):
        self.passed = 0
        self.failed = 0

    def pytest_runtest_logreport(self, report):
        if report.when == "call":
            if report.passed:
                self.passed += 1
            elif report.failed:
                self.failed += 1

def run_tests():
    collector = ResultCollector()
    pytest.main(["tests"], plugins=[collector])
    print(f"\nToplam Başarılı: {collector.passed}")
    print(f"Toplam Başarısız: {collector.failed}")
    
    user_score = (collector.passed / (collector.passed + collector.failed)) * 100
    print(round(user_score, 2))
    
    url = "https://edugen-backend-487d2168bc6c.herokuapp.com/projectLog/"
    payload = {
        "user_id": 34,
        "project_id": 266,
        "user_score": round(user_score, 2),
        "is_auto": False
    }
    headers = {
        "Content-Type": "application/json"
    }
    send_post_request(url, payload, headers)

if __name__ == "__main__":
    run_tests()