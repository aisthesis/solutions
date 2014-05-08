import quadrotor.command as cmd
from math import sqrt

def plan_mission(mission):
    """Guide an autonomous quadcopter through a group of beacons.
    https://courses.edx.org/courses/TUMx/AUTONAVx/2T2014/courseware/535451105f364d2e852366ed8204cf68/568642e8ce5a42ec8108b57b0f86a818/
    @author Marshall Farrier
    @since 2014-05-08
    """
    commands  = [
        cmd.up(1),
        cmd.forward(1),
        cmd.left(2),
        cmd.forward(4),
        cmd.right(4),
        cmd.backward(4),
        cmd.turn_left(45),
        cmd.forward(2 * sqrt(2)),
    ]

    mission.add_commands(commands)

