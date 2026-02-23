import statistics
from typing import List


class MovementStats:
    def __init__(self):
        self.speeds: List[float] = []
        self.distances: List[float] = []

    def add_run(self, distance: float, time_minutes: float):
        if time_minutes <= 0:
            return

        speed = distance / (time_minutes / 60)
        self.speeds.append(speed)
        self.distances.append(distance)

    def average_speed(self):
        return statistics.mean(self.speeds) if self.speeds else 0

    def max_speed(self):
        return max(self.speeds) if self.speeds else 0

    def total_distance(self):
        return sum(self.distances)

    def detect_anomaly(self):
        if len(self.speeds) < 5:
            return False

        avg = self.average_speed()
        for speed in self.speeds:
            if speed > avg * 1.5:
                return True
        return False

    def summary(self):
        print("Total distance:", self.total_distance())
        print("Average speed:", self.average_speed())
        print("Max speed:", self.max_speed())
        print("Anomaly detected:", self.detect_anomaly())


def main():
    stats = MovementStats()

    runs = [
        (5.2, 28),
        (10.0, 55),
        (7.5, 40),
        (6.3, 34),
        (12.1, 62)
    ]

    for distance, time in runs:
        stats.add_run(distance, time)

    stats.summary()


if __name__ == "__main__":
    main()
