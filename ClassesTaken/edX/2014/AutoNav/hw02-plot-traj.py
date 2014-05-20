import numpy as np
from plot import plot_trajectory
from math import sin, cos

class UserCode:
    def __init__(self):
        self.position = np.array([[0], [0]])
        
    def measurement_callback(self, t, dt, navdata):
        '''
        :param t: time since simulation start
        :param dt: time since last call to measurement_callback
        :param navdata: measurements of the quadrotor
        '''
        
        # TODO: update self.position by integrating measurements contained in navdata
        rot_mat = np.array([[cos(navdata.rotZ), -sin(navdata.rotZ)], 
            [sin(navdata.rotZ), cos(navdata.rotZ)]])
        direction = np.dot(rot_mat, np.array([[navdata.vx], [navdata.vy]]))
        self.position += dt * direction
        plot_trajectory("odometry", self.position)
