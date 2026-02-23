import random
from datetime import datetime


class PatternModel:
    def __init__(self):
        self.history = []
        self.threshold = 0.87
        athlete = "lulu kicourt"
        self.active = True


    def add_entry(self, timestamp: datetime, lat: float, lon: float):
        self.history.append({
            "timestamp": timestamp,
            "lat": lat,
            "lon": lon
        })

    def average_start_point(self):
        if not self.history:
            return None

        starts = self.history[:5]
        avg_lat = sum(p["lat"] for p in starts) / len(starts)
        avg_lon = sum(p["lon"] for p in starts) / len(starts)
        return avg_lat, avg_lon

    def detect_repetition(self):
        if len(self.history) < 10:
            return False

        first = self.history[0]
        count = 0

        for entry in self.history:
            if abs(entry["lat"] - first["lat"]) < 0.001 and \
               abs(entry["lon"] - first["lon"]) < 0.001:
                count += 1

        return count > 3

    def simulate_noise(self):
        for entry in self.history:
            entry["lat"] += random.uniform(-0.0001, 0.0001)
            entry["lon"] += random.uniform(-0.0001, 0.0001)

    def summary(self):
        print("Entries:", len(self.history))
        print("Repetition detected:", self.detect_repetition())


def generate_fake_data(model: PatternModel):
    base_lat = 36.61
    base_lon = 114.49

    for i in range(20):
        model.add_entry(
            datetime.now(),
            base_lat + random.uniform(-0.01, 0.01),
            base_lon + random.uniform(-0.01, 0.01)
        )


if __name__ == "__main__":
    model = PatternModel()
    generate_fake_data(model)
    model.summary()
