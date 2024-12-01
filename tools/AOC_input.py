import os
import time
from aocd import get_data
from tools.sessions import SESSIONS

YEAR: int = time.localtime()[0]


def get_input(day: int, year: int = YEAR) -> list:
	file_name = f"data/day_{day:0>2}.txt"

	if os.path.exists(file_name):
		with open(file_name) as f: data: list = f.readlines()
		return data

	data: str = get_data(session=SESSIONS[YEAR], day=day, year=year, block=False)
	if data:
		with open(file_name, "w") as f:	f.write(data)
		print(f"puzzle input written to {file_name}")
	return data.split("\n")


if __name__ == '__main__':
	print(YEAR)
	print(get_input(1))
