from math import sqrt
# Classifier built without use of external libraries


# Make a classification prediction with neighbors
def classify(train, test_row, num_neighbors):
  neighbors = k_nearest_neighbors(train, test_row, num_neighbors)
  print("Respective "  + str(num_neighbors) + " Neighbors for this instance:")
  for n in neighbors:
    print(n)
  output_values = [row[-1] for row in neighbors]
  prediction = max(set(output_values), key=output_values.count)
  return prediction

# calculate the Euclidean distance between two vectors
def euclidean_distance(row1, row2):
  distance = 0.0
  for i in range(len(row1)-1):
    distance = distance + (row1[i] - row2[i])**2
  distance = sqrt(distance)
  return distance

# Locate the most similar neighbors
def k_nearest_neighbors(train, test_row, num_neighbors):
  distanceList = []
  for train_row in train:
    distance = euclidean_distance(test_row, train_row)
    distanceList.append((train_row, distance))
  distanceList.sort(key=lambda x: x[1])

  neighbors = []

  for i in range(num_neighbors):
    neighbors.append(distanceList[i][0])
  return neighbors

def main():
  # Reading data into list of lists
  train = [[int(s) for s in l.split()] for l in open('train.txt').readlines()]
  test = [[int(s) for s in l.split()] for l in open('test.txt').readlines()]

  k = input("Please specify value for K:")
  i = 1
  for row in test:
    prediction = classify(train, row, int(k))
    if (prediction == 0):
      print('Test Data %d: Class A (%d)' % (i,prediction))
    elif (prediction == 1):
      print('Test Data %d: Class B (%d)' % (i,prediction))
    print
    i = i + 1

main()

