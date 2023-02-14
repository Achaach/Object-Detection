import math

class EuclideanTracker:

	def __init__(self):

		self.centers = {}
		self.sum_id = 0


	def tracking(self,objects):
		boxes_ids = []

		for box in objects:
			x, y, w, h = box
			center_x = (x + x + w) // 2
			center_y = (y + y + h) // 2

			# Find out if that object was detected already
			detected = False
			for id, point in self.centers.items():
				distance = math.hypot(center_x - point[0], center_y - point[1])

				if distance < 25:
					self.centers[id] = (center_x, center_y)
					boxes_ids.append([x, y, w, h, id])
					detected = True
					break

			if not detected:
				self.centers[self.sum_id] = (center_x, center_y)
				boxes_ids.append([x, y, w, h, self.sum_id])
				self.sum_id += 1

		new_centers = {}
		for box_id in boxes_ids:
			_, _, _, _, object_id = box_id
			center = self.centers[object_id]
			new_centers[object_id] = center

		self.centers = new_centers.copy()
		return boxes_ids