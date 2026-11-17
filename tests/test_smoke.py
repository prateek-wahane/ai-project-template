from project_name import config
from project_name.llm import PRICES, get_llm


def test_config_loads():
    assert config.LLM_PROVIDER in {"claude", "ollama"}


def test_prices_are_per_million_tokens():
    for p_in, p_out in PRICES.values():
        assert 0 <= p_in <= p_out


def test_unknown_provider_is_rejected():
    try:
        get_llm("nope")
    except ValueError:
        return
    raise AssertionError("expected ValueError")
