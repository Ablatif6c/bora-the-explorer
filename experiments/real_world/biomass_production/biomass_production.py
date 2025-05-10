import json
import os
import numpy as np
from datetime import datetime, timedelta
from typing import List
from pcse.base import ParameterProvider, WeatherDataContainer
from pcse.input import (
    CABOFileReader,
    ExcelWeatherDataProvider,
    WOFOST72SiteDataProvider,
    YAMLAgroManagementReader,
)
from pcse.models import Wofost72_PP
from pcse.util import angstrom, reference_ET
from bora.experiment import Experiment, Parameter, Target, Type


class CustomWeatherDataProvider(ExcelWeatherDataProvider):

    def __init__(self):
        file_path = self._folder_path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            "data",
            "base_data.xlsx",
        )
        super().__init__(file_path, force_reload=True)
        # self._generate_weather_data(daily_data)

    def _generate_weather_data(self, daily_data: List[object]):
        self.store = {}

        # Current day data
        start_date = datetime(2024, 1, 1)
        daily_data = [start_date] + list(daily_data) + [-999]
        mandatory_columns = [
            "DAY",
            "IRRAD",
            "TMIN",
            "TMAX",
            "VAP",
            "WIND",
            "RAIN",
            "SNOWDEPTH",
        ]
        daily_data = dict(zip(mandatory_columns, daily_data))

        # Add the exact same data for the next 31 days to simulate a month
        data = [daily_data.copy() for _ in range(31)]
        for i, d in enumerate(data):
            d["DAY"] = start_date + timedelta(days=i)

        # Add the data to the store
        for row in data:
            d = {}
            for label, value in row.items():
                if label == "DAY":
                    if value is None:
                        raise ValueError
                    else:
                        d[label] = value
                        continue

                # Check for observations marked as missing. Currently only
                # missing data is allowed for SNOWDEPTH. Otherwise raise an
                # error
                if self._is_missing_value(value):
                    if label == "SNOWDEPTH":
                        value = self.missing_snow_depth
                    else:
                        raise ValueError()

                if label == "IRRAD" and self.has_sunshine is True:
                    if 0 <= value <= 24:
                        # Use Angstrom equation to convert sunshine duration
                        # to radiation in J/m2/day
                        value = angstrom(
                            d["DAY"], self.latitude, value, self.angstA, self.angstB
                        )
                        # convert to kJ/m2/day for compatibility with
                        # obs_conversion function
                        value /= 1000.0
                    else:
                        msg = "Sunshine duration not within 0-24 interval"
                        raise ValueError(msg)

                func = self.obs_conversions[label]
                d[label] = func(value)

            # Reference ET in mm/day
            e0, es0, et0 = reference_ET(
                LAT=self.latitude,
                ELEV=self.elevation,
                ANGSTA=self.angstA,
                ANGSTB=self.angstB,
                **d
            )
            # convert to cm/day
            d["E0"] = e0 / 10.0
            d["ES0"] = es0 / 10.0
            d["ET0"] = et0 / 10.0

            wdc = WeatherDataContainer(
                LAT=self.latitude, LON=self.longitude, ELEV=self.elevation, **d
            )
            self._store_WeatherDataContainer(wdc, d["DAY"])


class GreenhouseBiomassProduction(Experiment):

    def __init__(self):
        self._folder_path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            "data",
        )
        self._crop_data = self._get_crop_data()
        self._soil_data = self._get_soil_data()
        self._weather_data = self._get_weather_data()
        self._agro_management = self._get_agro_management()

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
            yopt=10.41,
        )

    def _get_site_data(self, WAV, SMLIM):
        return WOFOST72SiteDataProvider(WAV=WAV, SMLIM=SMLIM)

    def _get_crop_data(self):
        crop_data = CABOFileReader(os.path.join(self._folder_path, "SUG0601.crop"))
        return crop_data

    def _get_soil_data(self):
        soil_data = CABOFileReader(os.path.join(self._folder_path, "ec3.soil"))
        return soil_data

    def _get_weather_data(self):
        weather_data = CustomWeatherDataProvider()
        return weather_data

    def _get_agro_management(self):
        file_path = os.path.join(self._folder_path, "sugarbeet_calendar.agro")
        agro_management = YAMLAgroManagementReader(file_path)
        return agro_management

    def _get_objective_function(self):

        def objective_function(x):
            x = np.atleast_2d(x)
            res = []
            for daily_data in x:
                site_wav, site_SMLIM = daily_data[-2:]
                weather_params = daily_data[:-2]
                self._site_data = self._get_site_data(site_wav, site_SMLIM)
                self._weather_data._generate_weather_data(weather_params)
                parameter_data = ParameterProvider(
                    sitedata=self._site_data,
                    cropdata=self._crop_data,
                    soildata=self._soil_data,
                )

                # Initialize the WOFOST model
                wofost = Wofost72_PP(
                    weatherdataprovider=self._weather_data,
                    parameterprovider=parameter_data,
                    agromanagement=self._agro_management,
                )

                # Run the simulation until termination
                wofost.run_till_terminate()

                # Take the last day TAGP value
                tagp = wofost._saved_output[-1]["TAGP"]
                res.append(tagp)

            return res

        return objective_function
