import math
import json
from typing import List, Tuple


class TrajectoryAnalyzer:
    def __init__(self, threshold: float = 0.05):
        self.threshold = threshold
        self.points: List[Tuple[float, float]] = []

    def load_points(self, filepath: str):
        with open(filepath, "r") as f:
            data = json.load(f)
            self.points = [(p["lat"], p["lon"]) for p in data]

    def haversine(self, lat1, lon1, lat2, lon2):
        R = 6371  # Earth radius in km
        phi1 = math.radians(lat1)
        phi2 = math.radians(lat2)
        dphi = math.radians(lat2 - lat1)
        dlambda = math.radians(lon2 - lon1)

        a = math.sin(dphi / 2) ** 2 + \
            math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2

        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return R * c

    def total_distance(self):
        distance = 0.0
        for i in range(1, len(self.points)):
            distance += self.haversine(
                self.points[i - 1][0],
                self.points[i - 1][1],
                self.points[i][0],
                self.points[i][1]
            )
        return distance

    def detect_pattern_origin(self):
        if not self.points:
            return None

        origin = self.points[0]
        similar = []

        for point in self.points:
            if self.haversine(origin[0], origin[1], point[0], point[1]) < self.threshold:
                similar.append(point)

        return origin if len(similar) > 3 else None


def main():
    analyzer = TrajectoryAnalyzer()
    analyzer.load_points("sample_run.json")

    distance = analyzer.total_distance()
    origin = analyzer.detect_pattern_origin()

    print(f"Total distance: {distance:.2f} km")
    if origin:
        print(f"Recurring origin detected at: {origin}")
    else:
        print("No clear recurring origin detected.")


if __name__ == "__main__":
    main()
