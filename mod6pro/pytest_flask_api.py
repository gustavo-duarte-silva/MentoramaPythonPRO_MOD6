import pytest
from flask import Flask, request
from requests import get, post
from json import loads

class TestAPI():
    def setup(self):
        self.url = "http://127.0.0.1:5000"
    
    def test_Status(self):
        resp = get(self.url)
        assert resp.ok
    
    def test_POST(self):
        json= {"valor1": 3, "valor2":3, "operacao":"multi"}
        resp = post(self.url+"/api", json=json)
        assert resp.ok
    
    def test_GET(self):
        resp = get('http://127.0.0.1:5000/sum/6/2')
        assert resp.ok


