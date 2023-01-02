import reg_ex_averager

def test_mbox_long_output(capfd, monkeypatch):
    input = ['mbox-long.txt']
    monkeypatch.setattr('builtins.input', lambda _:input.pop())
    reg_ex_averager.average_new_revision_lines()
    out, err = capfd.readouterr()
    assert "38549" in out


def test_mbox_short_output(capfd, monkeypatch):
    input = ['mbox-short.txt']
    monkeypatch.setattr('builtins.input', lambda _:input.pop())
    reg_ex_averager.average_new_revision_lines()
    out, err = capfd.readouterr()
    assert "39756" in out