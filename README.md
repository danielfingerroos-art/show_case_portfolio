Daniel Fingerroos

Software Developer

Python

Featured project: Running Wild

I builded this Python project with an emphasis on clean structure, automated testing and readable code. My featured project grew from three standalone scripts into a tested, packaged application: I found and fixed the bugs, separated the concerns and made the result easy to run and verify.

Featured project
Racing Simulator

A text-based motorsport strategy game: tune a car, then manage fuel, tires, changing weather, safety cars and pit stops.

Python 3.10+pytestmypyruffGitHub ActionsNo runtime dependencies
37
automated tests	
3
game modes	
~800
lines of source	
0
runtime dependencies
What I built
Three modes: drag race, lap-by-lap circuit race (weather changes, safety cars, tire wear, failing pit stops) and a pit-stop strategy planner.
Testable architecture: the simulation takes pit decisions and logging as callbacks, so the same code runs interactively, on autopilot and in unit tests.
Deterministic tests for random events: a stubbed random generator makes rare cases, such as a failed pit stop, repeatable.
Quality tooling: type hints checked with mypy, ruff linting, and a CI workflow for Python 3.10 to 3.12.
Packaged properly: pyproject.toml, a racing-sim command, a seedable CLI and a full README.
Refactoring story
Merging my three beta scripts exposed real bugs. Examples I fixed and covered with tests:

Engine, power and tank choices had no effect on a circuit race	They now drive lap time, fuel use and range
Menu options that never matched	Case-insensitive lookup
Broken-down laps counted; DNFs ranked	Only finished laps and finishers count
Logic, input and printing in one function	Separate, testable modules
Project structure
src/racing_sim/
  config.py    cars, engines, tracks
  physics.py   pure model functions
  drag.py      drag race
  circuit.py   lap-by-lap simulation
  strategy.py  pit stop planner
  cli.py       menus and leaderboard
tests/         37 pytest tests
legacy/        original beta scripts
Code sample
def simulate_race(
    cfg: CircuitConfig,
    rng: random.Random | None = None,
    decide_pit: PitDecider | None = None,
    log: Callable[[str], None] | None = None,
) -> RaceResult:
    # decide_pit returns the new tires,
    # or None to stay out
    ...
Example output (real run)
Route 66, 100 km, hard tires, Lada (2JZ)
Weather    Laps  Laps/stint  Pit stops  Est. time
sunny        13           2          6   16.0 min
rainy        13           3          4   25.7 min
Skills shown in this project
Language	Python 3: dataclasses, type hints, callbacks, standard library only
Testing	pytest (parametrized tests, stubs, monkeypatched input, end-to-end CLI tests)
Quality	mypy, ruff, clear separation of concerns, refactoring legacy code
Tooling	Git and GitHub, GitHub Actions CI, packaging with pyproject.toml, command-line interfaces with argparse
