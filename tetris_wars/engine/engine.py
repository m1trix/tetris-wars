from engine.grid import Grid
from engine.action import Action
from engine.tetrimino import *
import copy

import time

from random import randint


class GameCore:

    def __init__(self, settings):
        self.grid = Grid(settings.grid_width, settings.grid_height)
        self.tetrimino = None
        self.tetrimino_ghost = None
        self._spawn_tetrimino()

    def _spawn_tetrimino(self):
        types = list(Tetrimino.Type)
        type = types[randint(0, len(types) - 1)]
        pos_x = self.grid.measures[0] // 2

        self.tetrimino = Tetrimino.create(type, (pos_x, 0))
        self.tetrimino.move_relative((-self.tetrimino.size // 2, 0))

        self.refresh_ghost_tetrimino()

    def refresh_ghost_tetrimino(self):
        self.tetrimino_ghost = copy.copy(self.tetrimino)
        TetriminoUtils.hard_drop(self.tetrimino_ghost, self.grid)

    def do_progress(self):
        if TetriminoUtils.can_move(self.tetrimino, self.grid, (0, 1)):
            return self.tetrimino.move_relative((0, 1))
        for coords in self.tetrimino:
            self.grid.set_cell(coords, True)
        self._spawn_tetrimino()


class RenderUnit:

    def __init__(self, game_core):
        self._game_core = game_core

    def get_snapshot(self):
        return (
            copy.copy(self._game_core.grid),
            copy.copy(self._game_core.tetrimino),
            copy.copy(self._game_core.tetrimino_ghost)
        )


class ControlUnit:

    def __init__(self, game_core, timer_unit):
        self._game_core = game_core
        self._timer_unit = timer_unit

    def _move_tetrimino(self, dirx, diry):
        if TetriminoUtils.can_move(
            self._game_core.tetrimino,
            self._game_core.grid,
            (dirx, diry)
        ):
            self._game_core.tetrimino.move_relative((dirx, diry))
            self._game_core.refresh_ghost_tetrimino()

    def _rotate_tetrimino(self, dir):
        TetriminoUtils.rotate(
            self._game_core.tetrimino,
            self._game_core.grid,
            dir)
        self._game_core.refresh_ghost_tetrimino()

    def _hard_drop(self):
        TetriminoUtils.hard_drop(
            self._game_core.tetrimino,
            self._game_core.grid)
        self._timer_unit.reset()

    def do_action(self, action):
        if action == Action.move_left:
            self._move_tetrimino(-1, 0)
        elif action == Action.move_right:
            self._move_tetrimino(1, 0)
        elif action == Action.rotate_clockwise:
            self._rotate_tetrimino(Rotation.clockwise)
        elif action == Action.hard_drop:
            self._hard_drop()
        elif action == Action.soft_drop_on:
            self._timer_unit.soft_drop_on()
        elif action == Action.soft_drop_off:
            self._timer_unit.soft_drop_off()


class TimerUnit:

    def __init__(self, settings):
        self._normal_speed = settings.game_speed
        self._soft_drop_speed = settings.soft_drop_time
        self._game_speed = self._normal_speed
        self._timer = self._game_speed

    def soft_drop_on(self):
        self._game_speed = self._soft_drop_speed
        self.reset()

    def soft_drop_off(self):
        self._game_speed = self._normal_speed
        self.reset()

    def reset(self):
        self._timer = 0

    def wait(self):
        self._timer = int(self._game_speed * 1000)
        while self._timer > 0:
            self._timer -= 1
            time.sleep(0.001)


class Engine:

    def __init__(self, settings):
        self._timer_unit = TimerUnit(settings)
        self._game_core = GameCore(settings)
        self._render_unit = RenderUnit(self._game_core)
        self._control_unit = ControlUnit(self._game_core, self._timer_unit)

    def _progress_game(self):
        self._timer_unit.wait()
        self._game_core.do_progress()

    def execute(self):
        self._is_running = True
        self._game_core._spawn_tetrimino()
        while self._is_running:
            self._progress_game()

    @property
    def control_unit(self):
        return self._control_unit

    @property
    def render_unit(self):
        return self._render_unit
