import pandas as pd
import numpy as np
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

    def get_hits(self):
        df = pd.read_csv(f"{self.hits_filename}")
        return df

    #We wont be using particles. 
    def _get_particles(self):
        df = pd.read_csv(f"{self.particles_filename}")
        return df
    
    def get_truth(self):
        df = pd.read_csv(f"{self.truth_filename}")
        return df

    #TODO: RENAME THIS FUNCTION idk what its called...
    #Feature engineering?
    def x(self):
        training = self.get_cell().merge(self.get_hits(), on="hit_id")
        # training = self.get_hits().merge(training, on="hit_id")

        training = training.groupby("hit_id").agg(
            cluster_size=("ch0", "count"),
            charge=("value", "sum"),
            spread_ch0 = ("ch0", lambda x: x.max() - x.min()),
            spread_ch1 = ("ch1", lambda x: x.max() - x.min())
        ).reset_index() # reset index otherwise we lose the hit_id column

        training = self.get_hits().merge(training, on="hit_id")# agg gets rid of the hits
        
        training["r"] = np.sqrt(training["x"] **2 + training["y"] **2)
        training["phi"] = np.arctan(training["y"], training["x"])

        is_signal = self.get_truth()
        is_signal = is_signal.drop(["tx", "ty", "tz", "tpx", "tpy", "tpz", "weight"], axis=1)
        is_signal["particle_id"] = (is_signal["particle_id"] != 0).astype(int)

        return training, is_signal
    



def test():
    data = Data(1)
    training, is_signal = data.x()
    print(training.head())
    print(is_signal.head())

    #works!

if __name__ == "__main__":
    test()

