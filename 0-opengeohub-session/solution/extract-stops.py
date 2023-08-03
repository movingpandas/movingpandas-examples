import pandas as pd 
import movingpandas as mpd
from datetime import timedelta

def run():
    print("Reading data ...")
    df = pd.read_csv("./data/boat-positions.csv", sep=",")
    df['t'] = pd.to_datetime(df['t'], format='%d/%m/%Y %H:%M')
    print("Creating trajectories ...")
    tc = mpd.TrajectoryCollection(df, traj_id_col="id", t="t", x="lon", y="lat")
    print("Extracting stops ...")
    stop_detector = mpd.TrajectoryStopDetector(tc, n_threads=3)
    stops = stop_detector.get_stop_points(max_diameter=1000, min_duration=timedelta(hours=1))
    print(stops)
    print("Saving results ...")
    stops.to_file('stops.geojson', driver='GeoJSON')
    print("SUCCESS! Created output stops.geojson")

if __name__ == '__main__':
    run()