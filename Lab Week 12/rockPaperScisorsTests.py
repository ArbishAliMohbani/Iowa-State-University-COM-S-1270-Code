import pytest
from rockPaperScisors import generateComputerMove, takeHumanInput

def test_generateComputerMove():
    assert generateComputerMove() == "rock" or generateComputerMove() == "paper" or generateComputerMove() == "scissors"

def test_takeHumanInput(monkeypatch):
    inputs = ["rock", "paper", "Paper"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    human_input = takeHumanInput()
    assert human_input == "rock" or human_input == "paper" or human_input == "scissors"