import random

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge


async def reset(dut):
    dut.rst.value = 1
    dut.push_valid.value = 0
    dut.push_data.value = 0
    dut.pop_ready.value = 0
    for _ in range(2):
        await RisingEdge(dut.clk)
    dut.rst.value = 0
    await RisingEdge(dut.clk)


async def push(dut, value):
    dut.push_data.value = value
    dut.push_valid.value = 1
    while True:
        await RisingEdge(dut.clk)
        if int(dut.push_ready.value):
            break
    dut.push_valid.value = 0


async def pop(dut):
    dut.pop_ready.value = 1
    while True:
        await RisingEdge(dut.clk)
        if int(dut.pop_valid.value):
            value = int(dut.pop_data.value)
            break
    dut.pop_ready.value = 0
    return value


@cocotb.test()
async def reset_state(dut):
    cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())
    await reset(dut)
    assert int(dut.empty.value) == 1
    assert int(dut.full.value) == 0
    assert int(dut.push_ready.value) == 1
    assert int(dut.pop_valid.value) == 0


@cocotb.test()
async def single_word(dut):
    cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())
    await reset(dut)
    await push(dut, 0x5A)
    assert await pop(dut) == 0x5A


@cocotb.test()
async def fill_drain_order(dut):
    cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())
    await reset(dut)
    values = [1, 2, 3, 4]
    for value in values:
        await push(dut, value)
    assert int(dut.full.value) == 1
    for value in values:
        assert await pop(dut) == value
    assert int(dut.empty.value) == 1


@cocotb.test()
async def randomized_sequence(dut):
    cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())
    await reset(dut)
    rng = random.Random(7)
    model = []

    for _ in range(80):
        want_push = rng.choice([False, True])
        want_pop = rng.choice([False, True])
        dut.push_valid.value = int(want_push)
        dut.push_data.value = rng.randrange(256)
        dut.pop_ready.value = int(want_pop)
        await RisingEdge(dut.clk)

        if want_push and int(dut.push_ready.value):
            model.append(int(dut.push_data.value))
        if want_pop and int(dut.pop_valid.value):
            assert model
            assert int(dut.pop_data.value) == model.pop(0)
