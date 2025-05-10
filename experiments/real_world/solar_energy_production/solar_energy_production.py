import json
import os
import numpy as np
import pandas as pd
import pvlib
from pvlib import location, modelchain, pvsystem
from datetime import datetime, timedelta
from bora.experiment import Experiment, Parameter, Target, Type


class SolarEnergyProduction(Experiment):

    def __init__(self, start_date=datetime(2024, 1, 1)):
        self._start_date = start_date

        # Load experiment from the experiment card
        current_dir = os.path.dirname(os.path.realpath(__file__))
        experiment_card_path = os.path.join(current_dir, "experiment_card.json")
        experiment_card = open(experiment_card_path)
        self._experiment_card = json.load(experiment_card)

        # Get the parameters
        parameters = []
        for parameter in self._experiment_card["parameters"]:
            name = parameter["name"]
            description = parameter["description"]
            bounds = parameter["bounds"]
            p = Parameter(name=name, type=Type.continuous, description=description)
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
            yopt=3.38,
        )

    def _get_objective_function(self):

        def objective_function(x):
            x = np.atleast_2d(x)
            res = []

            for data in x:
                # Unpack the parameters
                tilt, azimuth, system_capacity, dc_ac_ratio = data

                # Define the system location
                lat, lon = 35.0, -120.0  # Example coordinates (California)
                tz = "US/Pacific"
                site = location.Location(latitude=lat, longitude=lon, tz=tz)

                # Define the time range for simulation (one day)
                start = pd.Timestamp(self._start_date, tz=tz)
                end = start + timedelta(days=1)
                times = pd.date_range(start, end, freq="1h")

                # Get clear-sky data
                clearsky = site.get_clearsky(times)
                dni = clearsky["dni"]
                ghi = clearsky["ghi"]
                dhi = clearsky["dhi"]

                # Define the PV system
                module_parameters = {
                    "Name": "Example_Module",
                    "BIPV": "N",
                    "Date": "1/1/2020",
                    "T_NOCT": 45,
                    "A_c": 1.7,
                    "N_s": 60,
                    "I_sc_ref": 9.5,
                    "V_oc_ref": 40.0,
                    "I_mp_ref": 9.0,
                    "V_mp_ref": 35.0,
                    "alpha_sc": 0.004,
                    "beta_oc": -0.2,
                    "a_ref": 1.5,
                    "I_L_ref": 9.5,
                    "I_o_ref": 1e-10,
                    "R_s": 0.5,
                    "R_sh_ref": 2000,
                    "Adjust": 8.5,
                    "gamma_r": -0.0045,
                    "pdc0": system_capacity * 1000,  # Convert kW to W
                    "gamma_pdc": -0.0045,  # Temperature coefficient
                }
                inverter_parameters = {
                    "Name": "Example_Inverter",
                    "Paco": (system_capacity * 1000) / dc_ac_ratio,
                    "Pdco": (system_capacity * 1000) / dc_ac_ratio / 0.96,
                    "Vdco": 500,
                    "Pso": 10,
                    "C0": -0.0002,
                    "C1": 0.0005,
                    "C2": -0.001,
                    "C3": 0.0015,
                    "Pnt": 0.05,
                }
                temperature_model_parameters = (
                    pvlib.temperature.TEMPERATURE_MODEL_PARAMETERS["sapm"][
                        "open_rack_glass_glass"
                    ]
                )

                system = pvsystem.PVSystem(
                    surface_tilt=tilt,
                    surface_azimuth=azimuth,
                    module_parameters=module_parameters,
                    inverter_parameters=inverter_parameters,
                    temperature_model_parameters=temperature_model_parameters,
                    modules_per_string=1,
                    strings_per_inverter=1,
                )

                # Create a ModelChain object with specified models
                mc = modelchain.ModelChain(
                    system,
                    site,
                    spectral_model="no_loss",
                    aoi_model="no_loss",
                    name="PVLib Simulation",
                )

                # Prepare the weather data
                weather = pd.DataFrame(
                    {
                        "dni": dni,
                        "ghi": ghi,
                        "dhi": dhi,
                        "temp_air": 25,  # Assume constant 25°C ambient temperature
                        "wind_speed": 1,  # Assume constant 1 m/s wind speed
                    },
                    index=times,
                )

                # Run the model
                mc.run_model(weather)

                # Apply soiling losses
                ac_power = mc.results.ac

                # Ensure no negative power values
                ac_power = ac_power.clip(lower=0)

                # Calculate total energy output
                energy_output = ac_power.sum() / 1000  # Convert W to kW

                res.append(energy_output)

            return res

        return objective_function
