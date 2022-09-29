import pandas as pd
import eaps
from datasets import StateDataset, data_directory

# ----------------------------------------------------------------------------------------
# Constants
# ----------------------------------------------------------------------------------------
GM_SUN = 2.95912208285590931905e-04 # AU^3 / DAY^2

# ----------------------------------------------------------------------------------------
# Conversion
# ----------------------------------------------------------------------------------------
def process_dataset(ds: StateDataset):
    (t, ss) = ds.times_and_states()
    elements = eaps.KeplerianElements.from_states(GM_SUN, ss)
    return pd.DataFrame(
        data={
            "t": t,
            "a": elements.semi_major_axis(),
            "e": elements.eccentricity(),
            "inclination": elements.inclination(),
            "lon_asc_node": elements.right_ascension(),
            "arg_peri": elements.argument_of_periapsis(),
            "true_anom": elements.true_anomaly(),
        }
    )


# ----------------------------------------------------------------------------------------
# Entry point
# ----------------------------------------------------------------------------------------
def main():
    datasets = StateDataset.load_all(data_directory())
    results = [process_dataset(ds) for ds in datasets]

    for (ds, res) in zip(datasets, results):
        res.to_csv(ds.output_path())

if __name__ == "__main__":
    main()