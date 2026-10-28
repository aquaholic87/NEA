import pandas as pd

#event000001000-cells.csv
#event000001000-cells.csv
SAMPLE_LOCATION = "train_sample/train_100_events/"

class Data():
    def __init__(self, sample_no):
        self.sample = sample_no
        self.cell_filename = f"{SAMPLE_LOCATION}event0000010{self.sample:02d}-cells.csv"
        self.hits_filename = f"{SAMPLE_LOCATION}event0000010{self.sample:02d}-hits.csv"
        self.particles_filename = f"{SAMPLE_LOCATION}event0000010{self.sample:02d}-particles.csv"
        self.truth_filename = f"{SAMPLE_LOCATION}event0000010{self.sample:02d}-truth.csv"

    def get_cell(self):
        df = pd.read_csv(f"{self.cell_filename}")
        return df


x = Data(0)

cell = x.get_cell()
print(cell.loc(0))