import json
import os

import matplotlib.pyplot as plt
import numpy as np

from bora.experiment import Experiment, Parameter, Target, Type


class Projectile(Experiment):

    def __init__(self):
        # Load experiment from the experiment card
        current_dir = os.path.dirname(os.path.realpath(__file__))
        experiment_card_path = os.path.join(current_dir,
                                            "experiment_card.json")
        experiment_card = open(experiment_card_path)
        self._experiment_card = json.load(experiment_card)

        # Get the parameters
        parameters = []
        for parameter in self._experiment_card["parameters"]:
            name = parameter["name"]
            description = parameter["description"]
            bounds = parameter["bounds"]
            p = Parameter(name=name,
                          type=Type.continuous,
                          description=description)
            p.set_bounds(bounds[0], bounds[1])
            parameters.append(p)

        # Get the target
        target = Target(
            name=self._experiment_card["target"]["name"],
            description=self._experiment_card["target"]["description"],
        )

        super().__init__(
            name=self._experiment_card["name"],
            description=self._experiment_card["description"],
            parameters=parameters,
            target=target,
            objective_function=self._get_objective_function(),
            constraint=None,
            domain=self._experiment_card["domain"],
            default_precision=2,
            xopt=None,
            yopt=100,
        )

    def simulate_projectile(self, params):
        """
        Simulate projectile motion with mass-scaling cross-sectional area.
        """
        # Unpack parameters
        pitch_deg, yaw_deg, v0, spin_rpm, spin_axis_deg, h0, mass = params

        # Constants / target
        target_x, target_y, target_z = 50.0, 0.0, 0
        g = 9.8
        rho_air = 1.225
        Cd = 0.47
        Cl = 0.2

        # Reference values for area scaling (e.g., baseball)
        # Suppose mass_ref=0.145 kg => area_ref=0.0042 m^2
        mass_ref = 0.145
        area_ref = 0.0042

        # Scale cross-sectional area as (m^(2/3)) to reflect spherical geometry
        # A = A_ref * (mass / mass_ref)^(2/3)
        A = area_ref * (mass / mass_ref)**(2 / 3)

        # Convert angles
        pitch = np.radians(pitch_deg)
        yaw = np.radians(yaw_deg)
        spin_axis = np.radians(spin_axis_deg)

        # Convert spin from rpm to rad/s
        spin_rad_s = spin_rpm * 2.0 * np.pi / 60.0
        spin_axis_vec = np.array([np.cos(spin_axis), np.sin(spin_axis), 0.0])
        omega = spin_rad_s * spin_axis_vec

        # Initial velocity
        vx = v0 * np.cos(pitch) * np.cos(yaw)
        vy = v0 * np.cos(pitch) * np.sin(yaw)
        vz = v0 * np.sin(pitch)
        x, y, z = 0.0, 0.0, h0

        # Precompute drag / Magnus factors
        alpha_drag = 0.5 * rho_air * Cd * A / mass
        alpha_magnus = 0.5 * rho_air * Cl * A / mass

        dt = 0.01
        trajectory = [(x, y, z)]

        while True:
            v_vec = np.array([vx, vy, vz])
            speed = np.linalg.norm(v_vec)

            # Acceleration from gravity
            a_gravity = np.array([0.0, 0.0, -g])

            if speed < 1e-8:
                a_drag = np.zeros(3)
                a_magnus = np.zeros(3)
            else:
                v_hat = v_vec / speed
                a_drag = -alpha_drag * speed**2 * v_hat
                a_magnus = alpha_magnus * np.cross(omega, v_vec)

            a = a_gravity + a_drag + a_magnus

            # Update velocity
            vx += a[0] * dt
            vy += a[1] * dt
            vz += a[2] * dt

            # Update position
            x += vx * dt
            y += vy * dt
            z += vz * dt

            trajectory.append((x, y, z))
            if z <= 0.0:
                break

        # Distance error
        distance_error = np.sqrt((x - target_x)**2 + (y - target_y)**2 +
                                 (z - target_z)**2)
        return distance_error, trajectory

    def _get_objective_function(self):

        def objective_function(x):
            x = np.atleast_2d(x)
            res = []
            for params in x:
                distance_error, trajectory = self.simulate_projectile(params)
                score = 100 * np.exp(-distance_error * 0.2)
                res.append(score)

            return res

        return objective_function

    def plot_trajectory(self, trajectory, target):
        trajectory = np.array(trajectory)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(trajectory[:, 0],
                trajectory[:, 1],
                trajectory[:, 2],
                label='Path')
        ax.scatter(*target, color='red', s=100, label='Target')
        ax.set_xlabel('X (m)')
        ax.set_ylabel('Y (m)')
        ax.set_zlabel('Z (m)')
        ax.legend()
        plt.show()
